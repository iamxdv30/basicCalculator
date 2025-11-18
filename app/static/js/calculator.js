/**
 * Calculator Application
 * Handles user interactions, calculations, and API communication
 */

// State management
const calculatorState = {
    currentValue: '0',
    previousValue: null,
    operation: null,
    waitingForOperand: false,
    history: []
};

// DOM Elements
const resultDisplay = document.getElementById('resultDisplay');
const operationDisplay = document.getElementById('operationDisplay');
const historyPanel = document.getElementById('historyPanel');
const historyList = document.getElementById('historyList');
const loading = document.getElementById('loading');

/**
 * Initialize calculator on page load
 */
document.addEventListener('DOMContentLoaded', () => {
    loadHistory();
    updateDisplay();
});

/**
 * Switch between basic and scientific modes
 */
function switchMode(mode) {
    const basicButtons = document.getElementById('basicButtons');
    const scientificButtons = document.getElementById('scientificButtons');
    const basicModeBtn = document.getElementById('basicMode');
    const scientificModeBtn = document.getElementById('scientificMode');

    if (mode === 'basic') {
        basicButtons.style.display = 'grid';
        scientificButtons.style.display = 'none';
        basicModeBtn.classList.add('active');
        scientificModeBtn.classList.remove('active');
    } else {
        basicButtons.style.display = 'none';
        scientificButtons.style.display = 'grid';
        basicModeBtn.classList.remove('active');
        scientificModeBtn.classList.add('active');
    }
}

/**
 * Insert value into display
 */
function insertValue(value) {
    if (value === 'pi') {
        calculatorState.currentValue = Math.PI.toString();
        calculatorState.waitingForOperand = false;
        updateDisplay();
        return;
    }

    if (calculatorState.waitingForOperand) {
        calculatorState.currentValue = value;
        calculatorState.waitingForOperand = false;
    } else {
        if (calculatorState.currentValue === '0' && value !== '.') {
            calculatorState.currentValue = value;
        } else {
            // Prevent multiple decimal points
            if (value === '.' && calculatorState.currentValue.includes('.')) {
                return;
            }
            calculatorState.currentValue += value;
        }
    }
    updateDisplay();
}

/**
 * Toggle sign of current value
 */
function toggleSign() {
    if (calculatorState.currentValue !== '0') {
        calculatorState.currentValue = (parseFloat(calculatorState.currentValue) * -1).toString();
        updateDisplay();
    }
}

/**
 * Clear display and reset state
 */
function clearDisplay() {
    calculatorState.currentValue = '0';
    calculatorState.previousValue = null;
    calculatorState.operation = null;
    calculatorState.waitingForOperand = false;
    updateDisplay();
}

/**
 * Backspace function
 */
function backspace() {
    if (calculatorState.currentValue.length > 1) {
        calculatorState.currentValue = calculatorState.currentValue.slice(0, -1);
    } else {
        calculatorState.currentValue = '0';
    }
    updateDisplay();
}

/**
 * Set basic operation (+, -, *, /)
 */
function setOperation(op) {
    if (calculatorState.previousValue !== null && calculatorState.operation !== null && !calculatorState.waitingForOperand) {
        calculate();
    }

    calculatorState.previousValue = calculatorState.currentValue;
    calculatorState.operation = op;
    calculatorState.waitingForOperand = true;
    updateDisplay();
}

/**
 * Set scientific operation (sin, cos, tan, cot, log, power, mod)
 */
function setScientificOperation(op) {
    calculatorState.operation = op;

    if (['sin', 'cos', 'tan', 'cot'].includes(op)) {
        // For trig operations, current value is the angle
        const angle = parseFloat(calculatorState.currentValue);
        const num1 = calculatorState.previousValue !== null ? parseFloat(calculatorState.previousValue) : null;

        performCalculation(op, { num1, angle });
    } else if (op === 'log') {
        // For log, we need number and base
        if (calculatorState.previousValue !== null) {
            const number = parseFloat(calculatorState.previousValue);
            const base = parseFloat(calculatorState.currentValue);
            performCalculation(op, { number, base });
        } else {
            // Default to log base 10
            const number = parseFloat(calculatorState.currentValue);
            const base = 10;
            performCalculation(op, { number, base });
        }
    } else if (op === 'power') {
        if (calculatorState.previousValue !== null) {
            calculatorState.waitingForOperand = true;
            updateDisplay();
        }
    } else if (op === 'mod') {
        if (calculatorState.previousValue !== null) {
            calculatorState.waitingForOperand = true;
            updateDisplay();
        } else {
            calculatorState.previousValue = calculatorState.currentValue;
            calculatorState.waitingForOperand = true;
            updateDisplay();
        }
    }
}

/**
 * Perform calculation
 */
async function calculate() {
    if (calculatorState.operation === null) {
        return;
    }

    const operation = calculatorState.operation;
    let data = {};

    // Prepare data based on operation type
    if (['+', '-', '*', '/'].includes(operation)) {
        data = {
            operation,
            num1: parseFloat(calculatorState.previousValue || calculatorState.currentValue),
            num2: parseFloat(calculatorState.currentValue)
        };
    } else if (['sin', 'cos', 'tan', 'cot'].includes(operation)) {
        data = {
            operation,
            num1: calculatorState.previousValue !== null ? parseFloat(calculatorState.previousValue) : null,
            angle: parseFloat(calculatorState.currentValue)
        };
    } else if (operation === 'log') {
        data = {
            operation,
            number: parseFloat(calculatorState.previousValue || calculatorState.currentValue),
            base: calculatorState.previousValue !== null ? parseFloat(calculatorState.currentValue) : 10
        };
    } else if (operation === 'power') {
        data = {
            operation,
            base: parseFloat(calculatorState.previousValue),
            exponent: parseFloat(calculatorState.currentValue)
        };
    } else if (operation === 'mod') {
        data = {
            operation,
            num1: parseFloat(calculatorState.previousValue),
            num2: parseFloat(calculatorState.currentValue)
        };
    }

    await performCalculation(operation, data);
}

/**
 * Perform API call to calculate
 */
async function performCalculation(operation, data) {
    showLoading();

    try {
        const response = await fetch('/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ operation, ...data })
        });

        const result = await response.json();

        if (result.success) {
            // Add to history
            addToHistory(result.operation, result.result);

            // Update display with result
            calculatorState.currentValue = result.result.toString();
            calculatorState.previousValue = null;
            calculatorState.operation = null;
            calculatorState.waitingForOperand = false;

            updateDisplay();
        } else {
            showError(result.error);
        }
    } catch (error) {
        showError('Network error: Unable to connect to server');
    } finally {
        hideLoading();
    }
}

/**
 * Update display
 */
function updateDisplay() {
    resultDisplay.textContent = formatNumber(calculatorState.currentValue);

    // Update operation display
    if (calculatorState.previousValue !== null && calculatorState.operation !== null) {
        let operationSymbol = calculatorState.operation;
        if (calculatorState.operation === '*') operationSymbol = '×';
        if (calculatorState.operation === '/') operationSymbol = '÷';

        operationDisplay.textContent = `${formatNumber(calculatorState.previousValue)} ${operationSymbol}`;
    } else {
        operationDisplay.textContent = '';
    }
}

/**
 * Format number for display
 */
function formatNumber(value) {
    if (value === null || value === undefined || value === '') {
        return '0';
    }

    const num = parseFloat(value);
    if (isNaN(num)) {
        return value;
    }

    // Format with appropriate precision
    if (Math.abs(num) < 0.000001 && num !== 0) {
        return num.toExponential(6);
    } else if (Math.abs(num) > 999999999) {
        return num.toExponential(6);
    } else {
        // Round to 10 decimal places to avoid floating point errors
        return parseFloat(num.toPrecision(12)).toString();
    }
}

/**
 * Show error message
 */
function showError(message) {
    operationDisplay.textContent = `Error: ${message}`;
    setTimeout(() => {
        operationDisplay.textContent = '';
    }, 3000);
}

/**
 * Show/hide loading indicator
 */
function showLoading() {
    loading.style.display = 'flex';
}

function hideLoading() {
    loading.style.display = 'none';
}

/**
 * Add calculation to history
 */
function addToHistory(operation, result) {
    const historyItem = {
        operation,
        result,
        timestamp: new Date().toISOString()
    };

    calculatorState.history.unshift(historyItem);

    // Keep only last 50 calculations
    if (calculatorState.history.length > 50) {
        calculatorState.history = calculatorState.history.slice(0, 50);
    }

    saveHistory();
    renderHistory();
}

/**
 * Render history list
 */
function renderHistory() {
    if (calculatorState.history.length === 0) {
        historyList.innerHTML = '<p class="empty-history">No calculations yet</p>';
        return;
    }

    historyList.innerHTML = calculatorState.history.map((item, index) => `
        <div class="history-item" onclick="useHistoryResult(${index})">
            <div class="history-operation">${escapeHtml(item.operation)}</div>
            <div class="history-result">= ${formatNumber(item.result)}</div>
        </div>
    `).join('');
}

/**
 * Use result from history
 */
function useHistoryResult(index) {
    const item = calculatorState.history[index];
    calculatorState.currentValue = item.result.toString();
    calculatorState.previousValue = null;
    calculatorState.operation = null;
    calculatorState.waitingForOperand = false;
    updateDisplay();
}

/**
 * Toggle history panel
 */
function toggleHistory() {
    if (historyPanel.style.display === 'none') {
        historyPanel.style.display = 'block';
        renderHistory();
    } else {
        historyPanel.style.display = 'none';
    }
}

/**
 * Clear history
 */
function clearHistory() {
    if (confirm('Are you sure you want to clear all history?')) {
        calculatorState.history = [];
        saveHistory();
        renderHistory();
    }
}

/**
 * Save history to localStorage
 */
function saveHistory() {
    try {
        localStorage.setItem('calculatorHistory', JSON.stringify(calculatorState.history));
    } catch (error) {
        console.error('Failed to save history:', error);
    }
}

/**
 * Load history from localStorage
 */
function loadHistory() {
    try {
        const saved = localStorage.getItem('calculatorHistory');
        if (saved) {
            calculatorState.history = JSON.parse(saved);
        }
    } catch (error) {
        console.error('Failed to load history:', error);
        calculatorState.history = [];
    }
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

/**
 * Keyboard support
 */
document.addEventListener('keydown', (event) => {
    const key = event.key;

    // Numbers and decimal point
    if (/^[0-9.]$/.test(key)) {
        insertValue(key);
    }
    // Operations
    else if (['+', '-', '*', '/'].includes(key)) {
        event.preventDefault();
        setOperation(key);
    }
    // Enter or equals
    else if (key === 'Enter' || key === '=') {
        event.preventDefault();
        calculate();
    }
    // Backspace
    else if (key === 'Backspace') {
        event.preventDefault();
        backspace();
    }
    // Escape or clear
    else if (key === 'Escape' || key.toLowerCase() === 'c') {
        event.preventDefault();
        clearDisplay();
    }
});

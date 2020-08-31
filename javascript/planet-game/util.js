// Rebinding common math functions
const PI = Math.PI
const frandom = Math.random
const min = Math.min
const max = Math.max
const floor = Math.floor
const ceil = Math.ceil
const round = Math.round
const pow = Math.pow
const hypot = Math.hypot
const sqrt = Math.sqrt
const bound = (low, val, high) => min(high, max(low, val))

function inRange(val, low, high) {
    return val >= low && val <= high 
}

function random(lower, upper) {
    let range = upper - lower + 1
    let n = floor(frandom() * range)
    return n + lower
}

// Even odds of returning 1 or -1
function randSign() {
    if (frandom() < 0.5) {
        return 1
    } else {
        return -1
    }
}

function randomVector(x0, x1, y0, y1) {
    return [random(x0,x1), random(y0,y1)]
}

function* xrange(upper) {
    for (let curr = 0; curr < upper; curr++) {
        yield curr
    }
}

function* xslice(arr, lower=0, upper) {
    let maximum = min(upper, arr.length)
    for (let i = lower; i < maximum; i++) {
        yield arr[i]
    }
}

function randomColor() {
    let r = random(0,255)
    let g = random(0,255)
    let b = random(0,255)

    return `rgb(${r},${g},${b})`
}

function randomElement(arr) {
    let index = random(0, arr.length - 1)
    return arr[index]
}
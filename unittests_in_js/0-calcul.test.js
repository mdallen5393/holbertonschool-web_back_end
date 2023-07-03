const assert = require('assert')
const calculateNumber = require('./0-calcul');

describe('My Function', function() {
  it('should round the numbers and return their sum', function() {
    const result = calculateNumber(1.5, 2.3);
    assert.equal(result, 4);
  });

  it('should round first number', function() {
    const result = calculateNumber(1.5, 2);
    assert.equal(result, 4);
  });

  it('should round second number', function() {
    const result = calculateNumber(1, 2.5);
    assert.equal(result, 4);
  });

  it('should round first number', function() {
    const result = calculateNumber(1.3, 2);
    assert.equal(result, 4);
  });

  it('should round second number', function() {
    const result = calculateNumber(1, 2.3);
    assert.equal(result, 4);
  });

  it('should work with integer values', function() {
    const result = calculateNumber(1, 4);
    assert.equal(result, 5);
  });

  it('should work with 0 values', function() {
    const result = calculateNumber(0, 0);
    assert.equal(result, 0);
  });

  it('should work with negative values', function() {
    const result = calculateNumber(-1, -32);
    assert.equal(result, -33);
  });

  it('should work with very large values', function() {
    const result = calculateNumber(Number.MAX_SAFE_INTEGER, 0.2);
    assert.equal(result, Number.MAX_SAFE_INTEGER);
  });
});
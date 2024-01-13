function isValidIranianNationalCode(input) {
  if (!/^\d{10}$/.test(input)) return false;
  const check = +input[9];
  const sum = input.split('').slice(0, 9).reduce((acc, x, i) => acc + +x * (10 - i), 0) % 11;
  return sum < 2 ? check === sum : check + sum === 11;
}

function isValidIranianNationalLegalCode(input) {
    if (!/^\d{11}$/.test(input)) return false;
    const check = +input[10];
    const decimal = +input[9]+2;
    const coefficient = [29,27,23,19,17,29,27,23,19,17]
    let sum = input.split('').slice(0, 10).reduce((acc, x, i) => acc + ((decimal + +x) * coefficient[i]), 0) % 11;
    if(sum==10)
        sum = 0;
    return sum === check;
}

const calculator = (str) => {
  let stack = [];
  let num = 0;
  let sign = "+";
  let index = 0;
  while (index < str.length) {
    if (str[index] === " ") {
      index++;
      continue;
    }
    if (!isNaN(str[index])) {
      num = num * 10 + parseInt(str[index]);
    }
    if (isNaN(str[index]) || index === str.length - 1) {
      if (sign === "+") {
        stack.push(num);
      } else if (sign === "-") {
        stack.push(-num);
      } else if (sign === "*") {
        stack.push(stack.pop() * num);
      } else if (sign === "/") {
        stack.push(parseInt(stack.pop() / num));
      }
      sign = str[index];
      num = 0;
    }
    index++;
  }
  return stack.reduce((acc, cur) => acc + cur);
};

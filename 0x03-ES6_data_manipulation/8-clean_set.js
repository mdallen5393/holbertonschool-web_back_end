export default function cleanSet(set, startString) {
  let newStr = "";
  for (const item in set) {
    if (item.startsWith(startString)) {
      newStr.concat(item.slice(startString.length));
    }
  }
}

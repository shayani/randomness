const test_size = 1_000_000

let zeros = 0
let ones = 0

for (let i = 0; i < test_size; i++) {
  if (Math.round(Math.random()) === 0) {
    zeros += 1
  } else {
    ones += 1
  }
}

const zeros_percentage = ((zeros / test_size) * 100).toFixed(3)
const ones_percentage = ((ones / test_size) * 100).toFixed(3)

console.log(`Generated ${test_size} random samples and got`)
console.log(`${zeros} (${zeros_percentage}%) zeros and`)
console.log(`${ones} (${ones_percentage}%) ones.`)

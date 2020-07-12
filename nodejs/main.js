//https://www.hackerrank.com/challenges/sock-merchant/problem
function sockMerchant(ar) {
    let s = new Set(ar);
    let counter = 0, pairs = 0;
    s.forEach((item) => {
        ar.forEach((a) => {
            if (item === a) {
                counter++;
            }
        });
        pairs += Math.floor(counter/2);
        counter = 0;
    });
    return pairs;
}

//https://www.hackerrank.com/challenges/drawing-book/problem
function pageCount(n, p) {
    let numberOfTurns = (n - 1) % 2 === 1 ? Math.floor((n - 1) / 2) + 1 : (n - 1) / 2;
    let numberOfTurnsFromStart = (p - 1) % 2 === 1 ? Math.floor((p - 1) / 2) + 1 : (p - 1) / 2;
    let numberOfTurnsFromEnd = numberOfTurns - numberOfTurnsFromStart;

    return numberOfTurnsFromStart > numberOfTurnsFromEnd ? numberOfTurnsFromEnd : numberOfTurnsFromStart;
}

const arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
console.log(pageCount(7, 2))
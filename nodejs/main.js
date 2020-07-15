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

//https://www.hackerrank.com/challenges/the-hurdle-race/problem
function hurdleRace(k, height) {
    const maxHeight = Math.max(...height);
    return k >= maxHeight ? 0 : maxHeight - k;
}

//https://www.hackerrank.com/challenges/angry-professor/problem
function angryProfessor(k, a) {
    let counter = 0;
    a.forEach((value) => {
        if (value <= 0) {
            counter++;
        }
    })
    return counter >= k ? 'NO' : 'YES';
}

//https://www.hackerrank.com/challenges/utopian-tree/problem
function utopianTree(n) {
    let height = 1;
    for (let i = 1; i <= n; i++) {
        if (i % 2 === 0) {
            height++;
        } else {
            height *= 2;
        }
    }
    return height;
}

console.log(utopianTree(55))
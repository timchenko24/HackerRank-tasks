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

const arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
console.log(sockMerchant(arr))
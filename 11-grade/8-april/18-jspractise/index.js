let fs = require('fs')

let input = fs.readFileSync('input.txt').toString().split('\r\n');

let arr = [];
input.forEach(element => {
    let temp = element.split(' ')
    arr.push({'arrive': Number(temp[0]), 'serveTime': Number(temp[1]), 'window': Number(temp[2])});
})
// let sortedArr = arr.sort(function (a, b) {
//     if (a.arrive > b.arrive) {
//         return 1;
//     }
//     if (a.arrive < b.arrive) {
//         return -1;
//     }
//     // a должно быть равным b
//     return 0;
// });

console.log(arr);

/*
[ 638, 13, 0 ],
Время прихода, время обслуживания, номер окна
 */
let countFor2 = 0;
let failedClients = 0;

let win1 = [];
let win2 = [];


function getWinNum(client) {
    let win1overflow = win1.length >= 14;
    let win2overflow = win2.length >= 14;
    neededWin = client["window"]

    switch (neededWin) {
        case 1: {
            return win1overflow ? -1 : 1;
        }
        case 2: {
            return win2overflow ? -1 : 2;
        }
        case 0:
            if (win2overflow && win1overflow) {
                return -1
            }
            if (win1overflow) {
                return 2
            }
            if (win2overflow) {
                return 1
            }
            return win1.length > win2.length ? 2 : 1
    }
}

function queuePush(client) {
    neededWin = getWinNum(client, win1, win2);
    console.log(`ОКНО: ${neededWin}`);
    if (neededWin == 1) {
        win1.push(client.serveTime)
    }
    if (neededWin == 2) {
        win2.push(client.serveTime);
        countFor2++;
    }
    if (neededWin == -1) {
        failedClients++
    }

}


function queueParse() {
    if (win1.length > 0) {
        win1[0]--

        if (win1[0] == 0) {
            win1.shift()
        }
    }
    if (win2.length > 0) {
        win2[0]--
        if (win2[0] == 0) {
            win2.shift()
        }
    }


    console.log(`Win1: ${win1}`)
}

// [
// [0, 21, 2, 3]

for (let time = 0; time < 1080; time++) {
    // console.log(time);
    let currentClient = arr.find(t => t.arrive === time);

    queueParse();

    if (currentClient === undefined) {
        continue;
    }
    console.log(currentClient)
    queuePush(currentClient)
    console.log(win1[1])

}


console.log(countFor2, failedClients)

/*
1. Взять клиента из Массива
2. Определяем номер окна (-1 = УШЁЛ)
3. Обработка очередей:
 -Уменьшаем минуты элемента 0
 -Когда элемент 0 равен 0, удаляем его из очереди + сдвигаем очередь
4. Ставим элемент в очередь (win1/2)
5. Счётчики
*/
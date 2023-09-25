const resultDiv = document.querySelector('.stopwatch__result');
const startBtn = document.querySelector('.stopwatch__buttons__start');
const stopBtn = document.querySelector('.stopwatch__buttons__stop');
const pauseBtn = document.querySelector('.stopwatch__buttons__pause');

let start;
let stop;
let pause = false;
let pauseTime = 0;
// let pauseStart;

startBtn.addEventListener('click', () => {
    start = new Date();
    resultDiv.innerHTML = ` `;
    console.log(start);
});

stopBtn.addEventListener('click', () => {
    stop = new Date();
    let res = stop - start;
    console.log(stop);
    console.log(res);
    if (pauseTime == 0) {
        resultDiv.innerHTML = returnResult(res);
    }
   else {
        resultDiv.innerHTML = returnResult(res - pauseTime);
        let pauseP = document.createElement('p');
        pauseP.innerHTML = `Пауза: ${pauseTime} мс`;
        resultDiv.append(pauseP);
        pauseTime = 0;
   }
})

pauseBtn.addEventListener('click', () => {
    if(!pause) {
        pauseStart = new Date();
        pauseBtn.classList.toggle('active');
        pause = true;
    } else {
        let pauseStop = new Date();
        pauseBtn.classList.toggle('active');
        pauseTime = pauseStop - pauseStart;
        pause = false;
    }
})

function returnResult(ms) {
    let mls = ms;
    let sec = 0;
    let min = 0;
    if (mls < 1000) return `Результат: ${mls} мс`;
    else if (mls >= 1000 && mls < 60000) {
        mls %= 1000;
        sec = Math.round(ms/1000);
        return `Результат: ${sec} сек ${mls} мс`;
    }
    else if(mls >= 60000) {
        min = Math.round(ms/60000);
        sec = Math.round(ms/1000);
        return `Результат: ${min} мин ${Math.round(mls/1000 - 60)} сек ${mls%1000} мс`;
    }
}


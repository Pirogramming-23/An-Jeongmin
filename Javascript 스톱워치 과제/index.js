let time = 0;
let timer = null;

const display = document.getElementById("display"); //시간 
const recordList = document.getElementById("recordlist"); //기록

document.querySelector(".start").addEventListener("click", () => {
    if (timer) return;
    timer = setInterval(() => {
        time++;
        updateDisplay();
    }, 10);
});

function updateDisplay() {
    display.innerText = formatTime(time);
}

function formatTime(time) {
    const sec = String(Math.floor(time / 100)).padStart(2, "0");
    const ms = String(time % 100).padStart(2, "0");
    return `${sec}:${ms}`;
}

document.querySelector(".stop").addEventListener("click", () => {
    clearInterval(timer);
    timer = null;
    addRecord();
});

function addRecord() {
    recordList.innerHTML += `
    <li>
        <div class="record-item">
        <input type="checkbox" />
        <span class="time">${formatTime(time)}</span>
        </div>
    </li>
    `;
}

document.querySelector(".reset").addEventListener("click", () => {
    clearInterval(timer);
    timer = null;
    time = 0;
    updateDisplay();
    recordList.innerHTML = ""; 
});

document.getElementById("deleteChecked").addEventListener("click", () => {
    const checkboxes = document.querySelectorAll("#recordlist input[type='checkbox']");
    checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
        checkbox.closest("li").remove();
        }
    });
});

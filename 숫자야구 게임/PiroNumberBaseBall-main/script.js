// 게임 초기화 
// 1단계 :	시도 횟수 9번 설정 , 확인할 때마다 감소
// 2단계 : 중복되지 않는 3개의 랜덤한 숫자 설정, html의 input과 결과창 내용 비우기
// 숫자 확인
// 3단계 : 버튼 누르면 입력 숫자 3개 확인
// 4단계 : 결과 계산 로직 및 html에 표시
// 5단계 : 3개 다 맞으면 게임 종료
// 6단계 : 시도 다 하면 실패
// 7단계 : 결과 표시하고 초기화

const attempts = {
    stage : 9
};

document.querySelector(".remaining-attempts").innerHTML =
`남은 횟수: <span id="attempts">${attempts.stage}</span>`;

const submit = document.getElementsByClassName("submit-button");
const first = document.getElementById("number1");
const second = document.getElementById("number2");
const third = document.getElementById("number3");

let answer = new Set();
while(answer.size<3){
    answer.add(Math.floor(Math.random()*10))
}

let answers = Array.from(answer);
console.log(answers);

function check_numbers(first, second, third){
    let strike = 0;
    let ball = 0;
    const user = [parseInt(first.value), parseInt(second.value), parseInt(third.value)];
    const used = [false, false, false];

    for (let i = 0; i < 3; i++) {
        if (user[i] === answers[i]){
            strike++;
            used[i]=true;
        }
    }

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (used[j]===false&&i !== j && user[i] === answers[j]) {
                ball++;
                break;
            }
        }
    }

    if(strike === 0 && ball === 0){
        document.querySelector(".result-display").innerHTML +=
        `   <div class="check-result">
                <div class="left">${user[0]} ${user[1]} ${user[2]}</div>
                <div class="left">:</div>
                <div class="out num-result left">O</div>
            </div>
        `;
    }

    else{
        document.querySelector(".result-display").innerHTML +=
        `   <div class="check-result">
                <div class="left">${user[0]} ${user[1]} ${user[2]}</div>
                <div class="left">:</div>
                <div class="left">${strike}
                <span class="strike num-result">S</span> 
                </div>
                <div class="left">${ball}
                <span class="ball num-result">B</span>
                </div>
            </div>
        `;
    }

    if(strike === 3){
        document.querySelector(".game-result").innerHTML = `
            <img src="./success.png" id="game-result-img" />`;
        submit[0].disabled = true;
        return;
    }
};

submit[0].onclick = () => {
    if(first.value !== ""&& second.value!=""&&third.value!==""){
        if(attempts.stage>1){
            attempts.stage -=1;
            document.querySelector(".remaining-attempts").innerHTML =
            `남은 횟수: <span id="attempts">${attempts.stage}</span>`
            check_numbers(first,second,third);
        }
        else{
            attempts.stage -=1;
            document.querySelector(".remaining-attempts").innerHTML =
            `남은 횟수: <span id="attempts">${attempts.stage}</span>`
            document.querySelector(".game-result").innerHTML = `
            <img src="./fail.png" id="game-result-img" />`;
            check_numbers(first,second,third);
            submit[0].disabled = true;
        }
    }
    first.value = "";
    second.value = "";
    third.value = "";
};


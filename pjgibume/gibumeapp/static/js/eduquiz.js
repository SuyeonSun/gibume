const questions = [

    {
        question: "향수 원료의 종류로 현대 향수의 대부분을 차지 하고 있는 것은?",
        optionA: "합성향로",
        optionB: "조합향로",
        optionC: "식물성 향로",
        optionD: "동물성 향로",
        correctOption: "optionB"
    },

    {
        question: "다음 중 향수의 구분으로 옳지 않은 것은?",
        optionA: "퍼퓸 (PERFUME)",
        optionB: "오드 콜로뉴 (EAU DE COLOGNE)",
        optionC: "오드 뚜왈렛 (EAU DE TOLETTE)",
        optionD: "오드 투 칼리스토 (EAU DE TO CALLISTO)",
        correctOption: "optionD"
    },

    {
        question: "향취의 구성으로 옳지 않은 것은?",
        optionA: "탑 노트",
        optionB: "미들 노트",
        optionC: "언더 노트",
        optionD: "베이스 노트",
        correctOption: "optionC"
    },

    {
        question: "다음 중 갈리마드 향수 계열이 아닌 것은?",
        optionA: "플로럴",
        optionB: "오리엔탈",
        optionC: "우디",
        optionD: "아쿠아린",
        correctOption: "optionD"
    },
    {
        question: "다음 중 향수를 보관하기 나쁜 곳은?",
        optionA: "파우더룸",
        optionB: "침실",
        optionC: "거실",
        optionD: "욕실",
        correctOption: "optionD"
    },

    {
        question: "다음 중 오드 투알렛 향수의 부향률로 적절한 것은?",
        optionA: "5-10%",
        optionB: "10-15%",
        optionC: "15-20%",
        optionD: "20-25%",
        correctOption: "optionA"
    },

    {
        question: "퍼퓸의 평균 지속시간은 ?",
        optionA: "6-7시간",
        optionB: "5시간",
        optionC: "3-4시간",
        optionD: "1-2시간",
        correctOption: "optionA"
    },

    {
        question: "다음 중 비슷한 향조별로 묶이지 않은 것은?",
        optionA: "장미, 튜베로즈",
        optionB: "우디, 머스크",
        optionC: "장미, 라일락",
        optionD: "우디, 바닐라",
        correctOption: "optionD"
    },

    {
        question: "다음 중 가장 오래 지속되는 향은?",
        optionA: "edc",
        optionB: "edt",
        optionC: "edp",
        optionD: " extrait de parfum (parfum)",
        correctOption: "optionD"
    },

    {
        question: "다음 중 시향지 보관에 적절하지 않은 곳은??",
        optionA: "책 사이",
        optionB: "다이어리",
        optionC: "지갑",
        optionD: "클리어 포켓",
        correctOption: "optionC"
    },

    {
        question: "향수의 지속성이 가장 약해지는 계절은 ?",
        optionA: "겨울",
        optionB: "봄",
        optionC: "여름",
        optionD: "가을",
        correctOption: "optionA"
    },


    {
        question: "향수의 지속력을 높이는 방법으로 옳지 않은 것은?",
        optionA: "38",
        optionB: "42",
        optionC: "40",
        optionD: "36",
        correctOption: "optionB"
    },

    {
        question: "4~6시간의 지속성을 가지며 부담스럽지 않은 향에 저렴한 가격을 가진 향수는?",
        optionA: "퍼퓸",
        optionB: "오 드 뜨왈렛",
        optionC: "오 드 코롱",
        optionD: "오 드 퍼퓸",
        correctOption: "optionD"
    },

    {
        question: "다음 중 베이스 노트로 적절하지 않은 향은?",
        optionA: "시트러스",
        optionB: "바닐라",
        optionC: "머스크",
        optionD: "우디",
        correctOption: "optionA"
    },

    {
        question: "향수를 사용하기 좋지 않은 장소는 ?",
        optionA: "손목",
        optionB: "목 뒤",
        optionC: "손등",
        optionD: "발목",
        correctOption: "optionC"
    },

    {
        question: "샤워 코롱의 향료 함량은?",
        optionA: "1% 미만",
        optionB: "1-2%",
        optionC: "2-5%",
        optionD: "5-10%",
        correctOption: "optionC"
    }

]


let shuffledQuestions = [] 

function handleQuestions() { 
    while (shuffledQuestions.length <= 9) {
        const random = questions[Math.floor(Math.random() * questions.length)]
        if (!shuffledQuestions.includes(random)) {
            shuffledQuestions.push(random)
        }
    }
}


let questionNumber = 1 
let playerScore = 0  
let wrongAttempt = 0 
let indexNumber = 0 


function NextQuestion(index) {
    handleQuestions()
    const currentQuestion = shuffledQuestions[index]
    document.getElementById("question-number").innerHTML = questionNumber
    document.getElementById("player-score").innerHTML = playerScore
    document.getElementById("display-question").innerHTML = currentQuestion.question;
    document.getElementById("option-one-label").innerHTML = currentQuestion.optionA;
    document.getElementById("option-two-label").innerHTML = currentQuestion.optionB;
    document.getElementById("option-three-label").innerHTML = currentQuestion.optionC;
    document.getElementById("option-four-label").innerHTML = currentQuestion.optionD;

}


function checkForAnswer() {
    const currentQuestion = shuffledQuestions[indexNumber]  
    const currentQuestionAnswer = currentQuestion.correctOption 
    const options = document.getElementsByName("option"); 
    let correctOption = null

    options.forEach((option) => {
        if (option.value === currentQuestionAnswer) {
            correctOption = option.labels[0].id
        }
    })

    //질문 답
    if (options[0].checked === false && options[1].checked === false && options[2].checked === false && options[3].checked == false) {
        document.getElementById('option-modal').style.display = "flex"
    }

    //질문 답 확인
    options.forEach((option) => {
        if (option.checked === true && option.value === currentQuestionAnswer) {
            document.getElementById(correctOption).style.backgroundColor = "hotpink"
            playerScore++ //점수 +
            indexNumber++ //질문 +

            setTimeout(() => {
                questionNumber++
            }, 1000)
        }

        else if (option.checked && option.value !== currentQuestionAnswer) {
            const wrongLabelId = option.labels[0].id
            document.getElementById(wrongLabelId).style.backgroundColor = "red"
            document.getElementById(correctOption).style.backgroundColor = "hotpink"
            wrongAttempt++ //adds 1 to wrong attempts 
            indexNumber++
            setTimeout(() => {
                questionNumber++
            }, 1000)
        }
    })
}




function handleNextQuestion() {
    checkForAnswer()
    unCheckRadioButtons()

    setTimeout(() => {
        if (indexNumber <= 9) {
            NextQuestion(indexNumber)
        }
        else {
            handleEndGame()
        }
        resetOptionBackground()
    }, 1000);
}

// 정답/ 오답 색
function resetOptionBackground() {
    const options = document.getElementsByName("option");
    options.forEach((option) => {
        document.getElementById(option.labels[0].id).style.backgroundColor = ""
    })
}

// 언체크 버트 
function unCheckRadioButtons() {
    const options = document.getElementsByName("option");
    for (let i = 0; i < options.length; i++) {
        options[i].checked = false;
    }
}

// 문제 풀이 완료 후
function handleEndGame() {
    let remark = null
    let remarkColor = null

    // 점수 개산
    if (playerScore <= 3) {
        remark = "향수에 대해서 더 알아가 볼까요?"
        remarkColor = "red"
    }
    else if (playerScore >= 4 && playerScore < 7) {
        remark = "좋아요:) 향수에 대해 어느정도 알고 있어요"
        remarkColor = "orange"
    }
    else if (playerScore >= 7) {
        remark = "향수에 대해서는 뭐든지 물어봐! 당신은 향수 전문가!"
        remarkColor = "pink"
    }
    const playerGrade = (playerScore / 10) * 100

    // score board 데이터
    document.getElementById('remarks').innerHTML = remark
    document.getElementById('remarks').style.color = remarkColor
    document.getElementById('grade-percentage').innerHTML = playerGrade
    document.getElementById('wrong-answers').innerHTML = wrongAttempt
    document.getElementById('right-answers').innerHTML = playerScore
    document.getElementById('score-modal').style.display = "flex"

}

//리셋
function closeScoreModal() {
    questionNumber = 1
    playerScore = 0
    wrongAttempt = 0
    indexNumber = 0
    shuffledQuestions = []
    NextQuestion(indexNumber)
    document.getElementById('score-modal').style.display = "none"
}

// 경고
function closeOptionModal() {
    document.getElementById('option-modal').style.display = "none"
}

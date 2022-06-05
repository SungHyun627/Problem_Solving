function solution(answers) {
    let pattern1 = [1,2,3,4,5];
    let pattern2 = [2,1,2,3,2,4,2,5];
    let pattern3 = [3,3,1,1,2,2,4,4,5,5];
    let correct = [0, 0, 0];
    let answer = [];
    
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] === pattern1[i % pattern1.length]) correct[0]++;
        if (answers[i] === pattern2[i % pattern2.length]) correct[1]++;
        if (answers[i] === pattern3[i % pattern3.length]) correct[2]++;
    }
    max_correct = Math.max(...correct)
    console.log(max_correct, correct)
    for (let i = 0; i < 3; i++) {
        if (max_correct == correct[i]) answer.push(i+1);
    }
    
    return answer;
}
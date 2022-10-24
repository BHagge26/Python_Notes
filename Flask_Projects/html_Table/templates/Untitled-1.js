const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected3 = true;

const queue4 = [];
const expected4 = true;

var count = 0
function socialDistancingEnforcer(queue) {
    for( var i = 0; i < queue.length; i++){
        if (i >= 5 && queue[i] === 1){
            if (count < 6){
                return false
            }
            else{
                count = 0
            }
        }
        else{
        count += 1 
        }
    }

}





console.log(socialDistancingEnforcer(queue1)) // false
console.log(socialDistancingEnforcer(queue2)) // true
console.log(socialDistancingEnforcer(queue3)) // true
console.log(socialDistancingEnforcer(queue4)) // true

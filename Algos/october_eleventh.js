function binarySearch(sortedNums, searchNum) {
    var start = 0;
    var end = sortedNums.length - 1;
    while (start <= end) {
        var mid = Math.floor((start + end) / 2)
        if (sortedNums[mid] == searchNum) {
            return countAdjacent(sortedNums, mid);
        }
        if (sortedNums[mid] > searchNum) {
            end = mid - 1;
        }
        else if (sortedNums[mid] < searchNum) {
            start = mid + 1;
        }
    }
    return false;
}

function countAdjacent(arr, index) {
    let count = 1;
    let elem = arr[index];
    let right = index + 1;
    let left = index - 1;
    while (arr[right] == elem) {
        count++;
        right++
    }
    while (arr[left] == elem) {
        count++;
        left--;
    }
    return count;
}


console.log(binarySearch(nums1, searchNum1)); // false
console.log(binarySearch(nums2, searchNum2)); // true (1 for bonus)
console.log(binarySearch(nums3, searchNum3)); // true (1 for bonus)

// bonus, how many times does the search num appear ?
console.log(binarySearch(nums4, searchNum4)); // 4









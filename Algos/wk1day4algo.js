/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcdddaaa";
  const expected1 = "a4b2cd3a3";
  const expected1b = "a4bbcd3a3";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "ccbb";
  const expected4 = "ccbb";
  
  const str5 = "abbbbbbbbbbbbbbbbb"
  const expected5 = "ab17"
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
    
    function encodeStr(str) {
        var newStr = ""
        var counter = 1
        for (var i =0; i < str.length;i++) {
            if (str[i]==str[i+1]){
                counter++
            } else {
                if (counter <= 1){
                    newStr += str[i]
                } else {
                    newStr+=(str[i]+counter)
                }
                counter=1
            }
        }
        if (newStr.length >= str.length){
            return str
        }
        return newStr
    }

  console.log(encodeStr(str1)) // Expected: a4bbcd3
  console.log(encodeStr(str2)) // Expected: ""
  console.log(encodeStr(str3)) // Expected: a
  console.log(encodeStr(str4)) // Expected: bbcc
  console.log(encodeStr(str5)) // Expected: ab17

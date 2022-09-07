/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    if (ransomNote.length > magazine.length) {
        return false;
    }
    const count = {};
    for (const m of magazine) {
        if (count[m]) {
            count[m] ++;
        } else {
        count[m] = 1;
        }
    }
    for (const r of ransomNote) {
        if (!count[r]) {
            return false;
        } else {
            count[r] --;
        }
        if (count[r] < 0) {
            return false;
        }
    }
    return true;
};
var isPowerOfTwo = (n) => {
    if (n == 0){
        return false
    }
    //bit operation to check for power of two
    return (n & (-n)) === n 
};
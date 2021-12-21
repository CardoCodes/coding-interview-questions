var twoSum = (nums, target) => {
    //initialize a hash map to store values
    const hashMap = new Map()

    //loop through the length of nums
    for(i = 0; i < nums.length; i++){
        const lookingFor = target - nums[i]

        //Check to see if what we are looking for exists in the map
        if(hashMap.has(lookingFor)){
            return [hashMap.get(lookingFor), i]
        }

        //#Use the current nums[i] and constant target to determine the second value needed i.e (9-2 = 7)
        hashMap.set(nums[i], i)
    }

    return null
}

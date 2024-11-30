/**
 * 动态打字效果函数
 * (select和element只能选择一个)
 * @param {Object} options - 配置选项
 * @param {string} options.select - 选择器，用于定位要显示文本的DOM元素("#id"或".class")
 * @param {string} options.element - DOM元素（Element对象）
 * @param {string[]} options.strings - 要依次显示的字符串数组
 * @param {boolean} [options.lifeLike=true] - 是否模拟真实打字速度
 * @param {boolean} [options.loop=true] - 是否循环显示字符串
 * @param {number} [options.min_speed=200] - 最小打字速度（毫秒）
 * @param {number} [options.max_speed=500] - 最大打字速度（毫秒）
 * @param {string} [options.callback_one_txt=null] - 每个字符打字结束后的回调函数
 * @param {Function} [options.callback=null] - 打字结束后的回调函数(不循环时有效)
 * 
 */
function typeit({select=null,element=null, strings, lifeLike = true, loop = false, min_speed = 200, max_speed = 500,callback_one_txt=null,callback=null}) {
    // 获取要显示文本的DOM元素
    let text_dom;
    if (element) {
        text_dom = element;
    }else{
        text_dom = document.querySelector(select);
    }

    // 当前要显示的字符串的第几个字符
    let index = 0;
    // 文本数组的下标
    let xiaBiao = 0;
    // 判断是要实现打字还是删除字效果，初始为真（打字）
    let huan = true;
    // 记录已经完成一轮的次数
    let completedRounds = 0;

    /**
     * 获取一个随机速度值
     * @param {number} min - 最小速度
     * @param {number} max - 最大速度
     * @returns {number} - 随机速度值
     */
    function getRandomSpeed(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    /**
     * 执行下一步操作：打字或删除字符
     */
    function nextStep() {
        if (huan) {
            // 给.text标签添加字符，用.slice方法
            text_dom.innerHTML = strings[xiaBiao].slice(0, ++index);
            // 如果当前字符串的所有字符都已显示，则开始删除字符
            if (index === strings[xiaBiao].length) {
                // 如果数组下标超过了最后一个字符串且不循环，则停止定时器
                if (!loop && xiaBiao >= strings.length-1) {
                    clearInterval(intervalId);
                    text_dom.classList.remove("typeit_text_css");
                    callback && callback();
                    return;
                }
                huan = false;
            }
        } else {
            // 给.text标签删除字符，用.slice方法
            text_dom.innerHTML = strings[xiaBiao].slice(0, index--);
            // 如果所有字符都已删除，则准备显示下一个字符串
            if (index < 0) {
                index = 0;
                huan = true;
                xiaBiao++;
                // 如果数组下标超过最后一个字符串，则重新从第一个字符串开始
                if (xiaBiao >= strings.length) {
                    xiaBiao = 0;
                    completedRounds++;
                }
            }
        }
        callback_one_txt && callback_one_txt();
        text_dom.innerHTML += '<span class="typeit_text_css"></span>';
        // 根据是否需要模拟真实打字速度来设置下次执行的时间间隔
        setTimeout(nextStep, lifeLike ? getRandomSpeed(min_speed, max_speed) : min_speed);
    }
    // 启动定时器，开始执行第一步操作
    let intervalId = setTimeout(nextStep, lifeLike ? getRandomSpeed(min_speed, max_speed) : min_speed);
}
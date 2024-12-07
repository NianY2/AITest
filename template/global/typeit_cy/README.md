# typeit_cy
## 介绍
简单的打字机

## 使用方法
```html
<!-- 引入 -->
<link rel="stylesheet" href="./typeit_cy/typeit_cy.css">
<script src="./typeit_cy/typeit_cy.js"></script>
```
```javascript
/**
 * 动态打字效果函数
 * (select和element只能选择一个)
 * @param {Object} options - 配置选项
 * @param {string} options.select - 选择器，用于定位要显示文本的DOM元素("#id"或".class")
 * @param {Object} options.element - DOM元素（Element对象）
 * @param {string[]} options.strings - 要依次显示的字符串数组
 * @param {boolean} [options.lifeLike=true] - 是否模拟真实打字速度
 * @param {boolean} [options.loop=true] - 是否循环显示字符串
 * @param {number} [options.min_speed=200] - 最小打字速度（毫秒）
 * @param {number} [options.max_speed=500] - 最大打字速度（毫秒）
 * @param {Function} [options.callback_one_txt=null] - 每个字符打字结束后的回调函数
 * @param {Function} [options.callback=null] - 打字结束后的回调函数(不循环时有效)
 */
typeit({
    select: '#title',
    strings: ['你好', '欢迎使用CYAI'],
    lifeLike: true,
    loop: false
});


const messageSpan = document.createElement('span');
messageSpan.className = `message ${type}_message`;
typeit({
    element: messageSpan,
    strings: [text],
    lifeLike: true,
    loop: false,
    min_speed: 0,
    max_speed: 200,
    max_line_length: 1,
    callback_one_txt: () => {
        messageContainer.scrollTop = messageContainer.scrollHeight; // 滚动到底部
    },
    callback: () => {
        messageContainer.scrollTop = messageContainer.scrollHeight; // 滚动到底部
    }
});
```

## 作者信息
* Name: CY
* QQ: 1871263099
* 邮箱：1871263099@qq.com
* CSDN博客：[https://blog.csdn.net/qq_59636442?type=blog](https://blog.csdn.net/qq_59636442?type=blog)
* Gitee:[https://gitee.com/REMOTE_CY](https://gitee.com/REMOTE_CY)
* Github:[https://github.com/NianY2](https://github.com/NianY2)
* GitCode[https://gitcode.com/qq_59636442](https://gitcode.com/qq_59636442)

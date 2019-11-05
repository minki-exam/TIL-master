function init() {
    const button = document.querySelector('#js-todo-button');
    const inputTag = document.querySelector('#js-todo-input');
    const reverseBtn = document.querySelector('#js-reverse-button');
    const saveBtn = document.querySelector('#js-save-button');
    const loadBtn = document.querySelector('#js-load-button');

    /*
    saveBtn.addEventListener('click', () => {
        if (confirm('save?')) {  // return 이 있어, 사용자가 '확인'을 누르면 true
            const todoArea = document.querySelector('#js-todo-area');
            const content = todoArea.innerHTML;  // innerTEXT 는 HTML 의 text 만 가져오는 거야
            localStorage.setItem('content', content);
            alert('saved!');
        }
    })
    */
    saveBtn.addEventListener('click', saveToLocalStorage)
    loadBtn.addEventListener('click', loadFromLocalStorage)
    reverseBtn.addEventListener('click', reverseTodoItems);

    button.addEventListener('click', () => {
        const inputArea = document.querySelector('#js-todo-input');
        createTodoCard(inputArea.value);
        inputArea.value = null;
    });

    inputTag.addEventListener('keydown', (e) => {
        if (e.which === 13) {
            const inputArea = document.querySelector('#js-todo-input');
            createTodoCard(inputArea.value);
            inputArea.value = null;
        }
    });
}

// Card 만들기
function createTodoCard (content) {
    if (content) {
        const cardArea = document.querySelector('#js-todo-area');

        const todo = document.createElement('div');
        todo.className = 'ui segment js-card';

        const wrapper = document.createElement('div');
        wrapper.className = 'ui checkbox';

        const checkBox = document.createElement('input');
        checkBox.type = 'checkbox';
        // 새로고침 이후에도 이벤트 리스너가 달리는지?
        checkBox.addEventListener('click', () => {
            if (checkBox.checked) {
                todo.classList.add('secondary');
                label.classList.add('done');
            } else {
                todo.classList.remove('secondary');
                label.classList.remove('done');
            }
        })

        const label = document.createElement('label');
        label.innerHTML = content;

        const deleteIcon = document.createElement('i');
        deleteIcon.className = 'icon close custom-icon';

        deleteIcon.addEventListener('click', () => {
            cardArea.removeChild(todo);
        })

        wrapper.appendChild(checkBox);
        wrapper.appendChild(label);
        todo.appendChild(wrapper);
        todo.appendChild(deleteIcon);
        cardArea.appendChild(todo);
    }
}

function saveToLocalStorage () {
    if (confirm('save?')) {  // return 이 있어, 사용자가 '확인'을 누르면 true
        const todoArea = document.querySelector('#js-todo-area');  // '.innerText' 뒤에 붙여주면 innerHTML 의 text 만 가져오는 거야
        // const content = todoArea.innerHTML;
        const content = todoArea.innerText;
        localStorage.setItem('content', content);
        alert('saved!');
    }
}

function loadFromLocalStorage () {
    if (confirm('load?')) {
        const todoArea = document.querySelector('#js-todo-area');
        const contents = localStorage.getItem('content').split('\n');
        for (let i=0; i<contents.length; i++) {
            createTodoCard(contents[i]);
        }
        // todoArea.innerHTML = content;
        alert('loaded!');
    }
}

function reverseTodoItems () {
    const todoArea = document.querySelector('#js-todo-area');
    const todos = Array.from(document.querySelectorAll('.js-card'));

    while (todoArea.firstChild) {
        todoArea.removeChild(todoArea.firstChild);
    }

    todos.reverse().forEach((todo) => {
        todoArea.appendChild(todo);
    });

}
init();

// function init() {
//     const button = document.querySelector('#js-todo-button');
//     const inputTag = document.querySelector('#js-todo-input');
//     const reverseBtn = document.querySelector('#js-reverse-button');

//     reverseBtn.addEventListener('click', () => {
//         const todoArea = document.querySelector('#js-todo-area');
//         const todos = Array.from(document.querySelectorAll('.js-card'));

//         while (todoArea.firstChild) {
//             todoArea.removeChild(todoArea.firstChild);
//         }

//         todos.reverse().forEach((todo) => {
//             todoArea.appendChild(todo);
//         });

//     });

//     button.addEventListener('click', ()=> {
//         const inputArea = document.querySelector('#js-todo-input');  // 위치 중요
//         createTodoCard(inputArea.value);
//         inputArea.value = null;
//     });

//     inputTag.addEventListener('keydown', (e) => {
//         if (e.which == 13) {
//             const inputArea = document.querySelector('#js-todo-input');  // 위치 중요
//             createTodoCard(inputArea.value);
//             inputArea.value = null;
//         }
//     });

//     //  Card 만들기
//     const createTodoCard = (content, completed=false) => {
//         const cardArea = document.querySelector('#js-todo-area');
        
//         const todo = document.createElement('div');
//         todo.className = 'ui segment js-card';
        
//         const wrapper = document.createElement('div');
//         wrapper.className = 'ui checkbox';

//         const checkBox = document.createElement('input');
//         checkBox.type = 'checkbox';

//         checkBox.addEventListener('click', () => {
//             if (checkBox.checked) {
//                 todo.classList.add('secondary');
//                 label.classList.add('done');
//             }
//             else {
//                 todo.classList.remove('secondary');
//                 label.classList.remove('done');
//             }
//         })

//         const label = document.createElement('label');
//         label.innerHTML = content;

//         const deleteIcon = document.createElement('i');
//         deleteIcon.className = 'icon close custom-icon';

//         deleteIcon.addEventListener('click', () => {
//             cardArea.removeChild(todo);
//         })

//         wrapper.appendChild(checkBox);
//         wrapper.appendChild(label);
//         todo.appendChild(wrapper);
//         todo.appendChild(deleteIcon);
//         cardArea.appendChild(todo);
//     };
// }
// init();
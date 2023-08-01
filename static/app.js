const $SCCRIPT_ROOT = 'http://127.0.0.1:5000/';
class Chatbox {
  constructor() {
    this.args = {
      openButton: document.querySelector(".chatbox__button"),
      chatbox: document.querySelector(".chatbox__support"),
      sendButton: document.querySelector(".send__button"),
    };
    this.state = false;
    this.message = [];
  }

  display() {
    const { openButton, chatbox, sendButton } = this.args;

    // Add a click event listener to the openButton
    openButton.addEventListener("click", () => this.toggleState(chatbox));

    // Add a click event listener to the sendButton
    sendButton.addEventListener("click", () => this.onSendButton(chatbox));

    // Find the input element within the chatbox and add a keyup event listener
    const node = chatbox.querySelector("input");
    node.addEventListener("keyup", ({ key }) => {
      if (key === "Enter") {
        this.onSendButton(chatbox);
      }
    });
    
  }

  toggleState(chatbox) {
    this.state = !this.state;

    // Show and hide the chatbox

    if (this.state) {
      chatbox.classList.add("chatbox--active");
    } else {
      chatbox.classList.remove("chatbox--active");
    }
  }

  onSendButton(chatbox) {
    const textField = chatbox.querySelector("input");
    const text1 = textField.value;
    if (text1 === "") {
      return;
    }
    let msg1 = { name: "User", message: text1 };
    this.message.push(msg1);

    //   http://127.0.0.1:5000/predict
    fetch($SCCRIPT_ROOT + "/predict", {
      method: "POST",
      body: JSON.stringify({ message: text1 }),
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((r) => r.json())
      .then((r) => {
        let msg2 = { name: "GCUF SE Bot", message: r.answer };
        this.message.push(msg2);
        this.updateChatText(chatbox);
        textField.value = "";
      })
      .catch((error) => {
        console.error("Error:", error);
        this.updateChatText(chatbox);
        textField.value = "";
      });
  }

  updateChatText(chatbox) {
    var html = '';
    this.message.slice().reverse().forEach(function (item, index) {
      if (item.name === "GCUF SE Bot") {
        html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
      } else {
        html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
      }
    });

    const chatmessage = chatbox.querySelector('.chatbox__messages');
    chatmessage.innerHTML = html;
  }
}

const chatbox = new Chatbox();
chatbox.display();
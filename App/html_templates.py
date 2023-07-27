css = '''
<style>
.chat-message {
  padding: 1.2rem;
  border-radius: 0.8rem;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.chat-message.user {
  background-color: #4f5d73;
}

.chat-message.bot {
  background-color: #6d7c92;
}

.chat-message .avatar {
  width: 15%;
}

.chat-message .avatar img {
  max-width: 50px;
  max-height: 50px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #fff;
}

.chat-message .message {
  width: 85%;
  padding: 0.5rem;
  color: #f0f0f0;
}
'''
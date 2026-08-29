function MessageInput({ value, onChange, onSend }) {
  function handleSubmit(event) {
    event.preventDefault();

    if (!value.trim()) {
      return;
    }

    onSend();
  }

  return (
    <form className="message-input" onSubmit={handleSubmit}>
      <input
        type="text"
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder="Ask about Durgesh..."
      />

      <button type="submit">
        Send
      </button>
    </form>
  );
}

export default MessageInput;
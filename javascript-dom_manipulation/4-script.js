document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.getElementById('add_item');
  const list = document.querySelector('.my_list');

  addItem.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });
});

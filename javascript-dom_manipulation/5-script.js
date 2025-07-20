document.addEventListener('DOMContentLoaded', () => {
  const updateBtn = document.getElementById('update_header');
  const header = document.querySelector('header');

  updateBtn.addEventListener('click', () => {
    header.textContent = 'New Header!!!';
  });
});

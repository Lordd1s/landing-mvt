// Определение функции для отображения модального окна
function showEasterEggModal() {
// Создаем модальное окно
const modal = document.createElement('div');
modal.classList.add('modal');
modal.innerHTML = `
    <div class="modal-content">
    <span class="close-modal" onclick="closeEasterEggModal()">&times;</span>
    <p>Поздравляю! Ты нашел пасхалку!</p>
    </div>
`;
document.body.appendChild(modal);
}

// Определение функции для закрытия модального окна
function closeEasterEggModal() {
const modal = document.querySelector('.modal');
if (modal) {
    modal.remove();
}
}

// Отслеживание нажатия на кнопку
document.getElementById('easter-egg').addEventListener('click', showEasterEggModal);


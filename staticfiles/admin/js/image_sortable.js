// static/admin/js/image_sortable.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('Initializing Sortable.js for image ordering...');

    function initSortable() {
        // Находим все tbody в inline-groups
        const inlineGroups = document.querySelectorAll('.inline-group');

        inlineGroups.forEach(function(group) {
            const tbody = group.querySelector('tbody');
            if (tbody && !tbody.classList.contains('sortable-initialized')) {
                console.log('Found tbody, initializing Sortable...');

                // Добавляем handles для перетаскивания
                const rows = tbody.querySelectorAll('tr');
                rows.forEach(function(row) {
                    if (!row.querySelector('.drag-handle')) {
                        const handleCell = document.createElement('td');
                        handleCell.className = 'drag-handle';
                        handleCell.innerHTML = '⣿';
                        handleCell.style.cssText = 'width: 30px; cursor: grab; text-align: center; vertical-align: middle; border-right: 1px solid #ddd;';
                        row.insertBefore(handleCell, row.firstChild);
                    }
                });

                // Инициализируем Sortable.js
                const sortable = new Sortable(tbody, {
                    handle: '.drag-handle',
                    animation: 150,
                    ghostClass: 'sortable-ghost',
                    chosenClass: 'sortable-chosen',
                    dragClass: 'sortable-drag',
                    onStart: function(evt) {
                        evt.item.style.backgroundColor = '#f0f8ff';
                        document.querySelectorAll('.drag-handle').forEach(function(handle) {
                            handle.style.cursor = 'grabbing';
                        });
                    },
                    onEnd: function(evt) {
                        evt.item.style.backgroundColor = '';
                        document.querySelectorAll('.drag-handle').forEach(function(handle) {
                            handle.style.cursor = 'grab';
                        });
                        updateOrderNumbers(tbody);
                        saveNewOrder(tbody);
                    }
                });

                tbody.classList.add('sortable-initialized');
            }
        });
    }

    function updateOrderNumbers(tbody) {
        const rows = tbody.querySelectorAll('tr');
        rows.forEach(function(row, index) {
            const positionInput = row.querySelector('input[id$="-position"]');
            if (positionInput) {
                positionInput.value = index;
                // Триггерим событие изменения
                const event = new Event('change', { bubbles: true });
                positionInput.dispatchEvent(event);
            }
        });
        console.log('Order numbers updated');
    }

    function saveNewOrder(tbody) {
        const rows = tbody.querySelectorAll('tr');
        const order = [];
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        rows.forEach(function(row) {
            const idInput = row.querySelector('input[id$="-id"]');
            if (idInput && idInput.value) {
                order.push(idInput.value);
            }
        });

        console.log('Saving order:', order);

        if (order.length > 0) {
            fetch('update_image_order/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'order[]': order,
                    'csrfmiddlewaretoken': csrfToken
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Order saved successfully');
                showNotification('Порядок изображений сохранен', 'success');
            })
            .catch(error => {
                console.error('Error saving order:', error);
                showNotification('Ошибка при сохранении порядка', 'error');
            });
        }
    }

    function showNotification(message, type) {
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 12px 20px;
            background: ${type === 'success' ? '#d4edda' : '#f8d7da'};
            color: ${type === 'success' ? '#155724' : '#721c24'};
            border: 1px solid ${type === 'success' ? '#c3e6cb' : '#f5c6cb'};
            border-radius: 4px;
            z-index: 10000;
            font-family: Arial, sans-serif;
            font-size: 14px;
        `;
        notification.textContent = message;
        document.body.appendChild(notification);

        setTimeout(function() {
            notification.remove();
        }, 3000);
    }

    // Инициализируем при загрузке
    setTimeout(initSortable, 500);

    // Также инициализируем при изменении DOM (для динамически добавленных форм)
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                setTimeout(initSortable, 300);
            }
        });
    });

    if (document.body) {
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }
});

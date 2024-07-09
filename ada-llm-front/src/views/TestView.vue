<template>
    <div class="history-sidebar">
        <div class="history-header">
            Chat History
        </div>
        <ul class="history-list">
            <li v-for="(message, index) in history" :key="index" class="history-item">
                {{ message }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'HistorySidebar',
    props: {
        history: {
            type: Array,
            required: true,
        },
    },
};
</script>

<style scoped>
.history-sidebar {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    width: 300px;
    background-color: #f9f9f9;
    border-left: 1px solid #ccc;
    padding: 20px;
    overflow-y: auto;
}

.history-header {
    font-weight: bold;
    padding-bottom: 10px;
    border-bottom: 1px solid #ccc;
    margin-bottom: 10px;
}

.history-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.history-item {
    padding: 5px;
    border-radius: 5px;
    background-color: #e0e0e0;
    margin-bottom: 5px;
}
</style>
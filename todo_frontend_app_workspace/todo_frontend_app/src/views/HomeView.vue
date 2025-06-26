<script setup lang="ts">
import { ref, onMounted } from 'vue'

// API base. Replace with your deployment endpoint if necessary.
const API_BASE = import.meta.env.VITE_TODO_API_BASE || "http://localhost:3001"

type Task = {
  id: number;
  title: string;
  completed: boolean;
}

const tasks = ref<Task[]>([])
const newTask = ref('')
const editingId = ref<number | null>(null)
const editingText = ref('')

const loading = ref(false)
const error = ref<string | null>(null)

// PUBLIC_INTERFACE
async function fetchTasks() {
  loading.value = true
  error.value = null
  try {
    const resp = await fetch(`${API_BASE}/tasks`)
    if (!resp.ok) throw new Error('Failed to fetch tasks')
    tasks.value = await resp.json()
  } catch (e: unknown) {
    if (e instanceof Error) error.value = e.message
    else error.value = 'Could not load tasks'
  } finally {
    loading.value = false
  }
}

// PUBLIC_INTERFACE
async function addTask() {
  const title = newTask.value.trim()
  if (!title) return
  loading.value = true
  error.value = null
  try {
    const resp = await fetch(`${API_BASE}/tasks`, {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title })
    })
    if (!resp.ok) throw new Error('Could not add task')
    newTask.value = ''
    await fetchTasks()
  } catch (e: unknown) {
    if (e instanceof Error) error.value = e.message
    else error.value = 'Could not add task'
  } finally {
    loading.value = false
  }
}

// PUBLIC_INTERFACE
async function updateTask(id: number, title: string) {
  loading.value = true
  error.value = null
  try {
    const resp = await fetch(`${API_BASE}/tasks/${id}`, {
      method: "PUT",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title })
    })
    if (!resp.ok) throw new Error('Could not update task')
    editingId.value = null
    editingText.value = ''
    await fetchTasks()
  } catch (e: unknown) {
    if (e instanceof Error) error.value = e.message
    else error.value = 'Could not update task'
  } finally {
    loading.value = false
  }
}

// PUBLIC_INTERFACE
async function deleteTask(id: number) {
  loading.value = true
  error.value = null
  try {
    const resp = await fetch(`${API_BASE}/tasks/${id}`, { method: "DELETE" })
    if (!resp.ok) throw new Error('Could not delete task')
    await fetchTasks()
  } catch (e: unknown) {
    if (e instanceof Error) error.value = e.message
    else error.value = 'Could not delete task'
  } finally {
    loading.value = false
  }
}

// PUBLIC_INTERFACE
async function markCompleted(id: number, completed: boolean) {
  loading.value = true
  error.value = null
  try {
    const resp = await fetch(`${API_BASE}/tasks/${id}/complete`, {
      method: "PATCH",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ completed })
    })
    if (!resp.ok) throw new Error('Could not change status')
    await fetchTasks()
  } catch (e: unknown) {
    if (e instanceof Error) error.value = e.message
    else error.value = 'Could not update status'
  } finally {
    loading.value = false
  }
}

function startEditing(task: Task) {
  editingId.value = task.id
  editingText.value = task.title
}

function cancelEditing() {
  editingId.value = null
  editingText.value = ''
}

function handleKeyup(e: KeyboardEvent, task: Task) {
  if (e.key === "Enter") {
    if (editingText.value.trim()) {
      updateTask(task.id, editingText.value.trim())
    }
  } else if (e.key === "Escape") {
    cancelEditing()
  }
}

// Change handler for checkbox that is safe for TS
function handleCompletedChange(event: Event, task: Task) {
  const target = event.target as HTMLInputElement | null
  if (!target) return
  markCompleted(task.id, target.checked)
}

onMounted(() => fetchTasks())
</script>

<template>
  <main class="todo-dashboard">
    <section class="todo-header">
      <h1>To-Do List</h1>
      <form @submit.prevent="addTask" class="todo-input">
        <input
          v-model="newTask"
          :disabled="loading"
          type="text"
          placeholder="Add a new task..."
          autocomplete="off"
          aria-label="New task"
        />
        <button
          :disabled="loading || !newTask.trim()"
          type="submit"
          class="add-btn"
        >Add</button>
      </form>
    </section>

    <section class="todo-body">
      <ul class="tasks-list" v-if="tasks.length">
        <li v-for="task in tasks" :key="task.id"
            :class="{ completed: task.completed }">
          <div class="task-content">
            <input
              type="checkbox"
              :checked="task.completed"
              @change="handleCompletedChange($event, task)"
              :disabled="loading"
            />
            <template v-if="editingId === task.id">
              <input
                v-model="editingText"
                @keyup="e => handleKeyup(e, task)"
                type="text"
                class="edit-input"
                :disabled="loading"
                @blur="cancelEditing"
                maxlength="100"
                autofocus
              />
            </template>
            <template v-else>
              <span @dblclick="startEditing(task)" class="task-title">
                {{ task.title }}
              </span>
            </template>
          </div>
          <div class="actions">
            <button
              @click="startEditing(task)"
              v-if="editingId !== task.id"
              title="Edit"
              :disabled="loading"
              class="action-btn secondary"
            >Edit</button>
            <button
              @click="() => updateTask(task.id, editingText)"
              v-if="editingId === task.id"
              :disabled="loading || !editingText.trim()"
              class="action-btn accent"
            >Save</button>
            <button
              @click="cancelEditing"
              v-if="editingId === task.id"
              :disabled="loading"
              class="action-btn secondary"
            >Cancel</button>
            <button
              @click="() => deleteTask(task.id)"
              :disabled="loading"
              class="action-btn danger"
              title="Delete"
            >Delete</button>
          </div>
        </li>
      </ul>
      <div v-else class="empty-message">
        <span>No tasks yet. Start by adding one!</span>
      </div>
    </section>
    <div v-if="error" class="error-msg">{{ error }}</div>
  </main>
</template>

<style scoped>
.todo-dashboard {
  background: #fff;
  max-width: 400px;
  margin: 4rem auto 0;
  box-shadow: 0 4px 18px 0 rgba(45, 55, 72, .06);
  border-radius: 14px;
  padding: 2rem 1.5rem 1.5rem 1.5rem;
  font-family: inherit;
  color: #2D3748;
}
.todo-header h1 {
  color: #2D3748;
  font-size: 2.2rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 1.6rem;
}
.todo-input {
  display: flex;
  gap: 0.5rem;
}
.todo-input input[type="text"] {
  flex: 1;
  font-size: 1rem;
  border: 1px solid #A0AEC0;
  border-radius: 6px;
  padding: 0.7em 0.7em;
  background: #fafbfc;
  transition: border-color 0.2s;
  color: #2D3748;
}
.todo-input input[type="text"]:focus {
  border-color: #38B2AC;
  outline: none;
}
.add-btn {
  background: #38B2AC;
  color: #fff;
  font-weight: 600;
  border: none;
  border-radius: 6px;
  padding: 0 1rem;
  transition: background 0.15s;
  cursor: pointer;
}
.add-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.todo-body {
  margin-top: 2rem;
}
.tasks-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.tasks-list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.7rem 0;
  border-bottom: 1px solid #e7e7ea;
  transition: background 0.15s;
}
.tasks-list li:last-child {
  border-bottom: none;
}
.task-content {
  display: flex;
  align-items: center;
  flex: 1 1 auto;
  gap: 0.8em;
}
.tasks-list input[type="checkbox"] {
  accent-color: #38B2AC;
  width: 1.1rem;
  height: 1.1rem;
}
.task-title {
  font-size: 1.05rem;
  cursor: pointer;
  color: #2D3748;
  word-break: break-all;
  padding: 0.18rem 0;
}
.completed .task-title {
  text-decoration: line-through;
  color: #A0AEC0;
}
.edit-input {
  font-size: 1rem;
  border: 1px solid #A0AEC0;
  border-radius: 6px;
  padding: 0.45em 0.7em;
  width: 13em;
  margin-right: 0.5rem;
  color: #2D3748;
  background: #fafbfc;
}
.actions {
  display: flex;
  gap: 0.5rem;
}
.action-btn {
  font-size: 0.95rem;
  background: #E7ECEC;
  color: #2D3748;
  border: none;
  border-radius: 6px;
  padding: 0 0.7rem;
  height: 2rem;
  cursor: pointer;
  transition: background 0.15s;
}
.action-btn.secondary {
  background: #A0AEC0;
  color: #fff;
}
.action-btn.accent {
  background: #38B2AC;
  color: #fff;
}
.action-btn.danger {
  background: transparent;
  color: #eb5757;
  border: 1px solid #eb5757;
}
.action-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.empty-message {
  text-align: center;
  color: #A0AEC0;
  font-weight: 500;
  margin-top: 2rem;
}
.error-msg {
  margin-top: 1.5rem;
  padding: 0.8em 1em;
  color: #fff;
  background: #eb5757;
  border-radius: 8px;
  text-align: center;
  font-size: 1rem;
}
@media (max-width: 520px) {
  .todo-dashboard {
    max-width: 98vw;
    padding: 1.2rem 0.3rem;
  }
  .task-title, .edit-input {
    font-size: 0.97rem;
  }
}
</style>

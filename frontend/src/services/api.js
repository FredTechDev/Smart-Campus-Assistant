import axios from 'axios'

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Students API
export const studentAPI = {
  list: () => api.get('/students/'),
  get: (id) => api.get(`/students/${id}`),
  create: (data) => api.post('/students/', data),
  update: (id, data) => api.put(`/students/${id}`, data),
  getPerformance: (id) => api.get(`/students/${id}/performance`),
}

// Attendance API
export const attendanceAPI = {
  getAnalytics: (params) => api.get('/attendance/analytics', { params }),
  recordAttendance: (data) => api.post('/attendance/record', data),
  getStudentAttendance: (studentId, params) =>
    api.get(`/attendance/${studentId}`, { params }),
}

// Courses API
export const coursesAPI = {
  list: () => api.get('/courses/'),
  getRecommendations: (studentId, params) =>
    api.get(`/courses/recommendations/${studentId}`, { params }),
  create: (data) => api.post('/courses/', data),
}

// Chatbot API
export const chatbotAPI = {
  sendMessage: (data) => api.post('/chatbot/query', data),
  getHistory: (studentId, params) =>
    api.get(`/chatbot/history/${studentId}`, { params }),
}

export default api

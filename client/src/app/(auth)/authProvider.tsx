import axios from 'axios';

const API_BASE_URL = 'YOUR_API_BASE_URL'; // Replace with your actual API base URL

const auth = {
    // Register a new user
    register: async (userData) => {
        try {
            const response = await axios.post(`${API_BASE_URL}/users`, userData);
            return response.data;
        } catch (error) {
            throw error.response?.data || error.message;
        }
    },

    // Login and get token
    login: async (credentials) => {
        try {
            const response = await axios.post(`${API_BASE_URL}/api/token/`, credentials);
            // Store the token in localStorage
            if (response.data.access) {
                localStorage.setItem('token', response.data.access);
                if (response.data.refresh) {
                    localStorage.setItem('refreshToken', response.data.refresh);
                }
            }
            return response.data;
        } catch (error) {
            throw error.response?.data || error.message;
        }
    },

    // Get the stored token
    getToken: () => {
        return localStorage.getItem('token');
    },

    // Check if user is authenticated
    isAuthenticated: () => {
        return !!localStorage.getItem('token');
    },

    // Logout user
    logout: () => {
        localStorage.removeItem('token');
        localStorage.removeItem('refreshToken');
    },

    // Create axios instance with authentication header
    getAuthenticatedAxios: () => {
        const token = auth.getToken();
        return axios.create({
            baseURL: API_BASE_URL,
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
    }
};

export default auth;
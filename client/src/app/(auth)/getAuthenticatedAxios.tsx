// Example usage:

// Registration
try {
    const userData = {
        username: 'user123',
        password: 'password123',
        email: 'user@example.com'
    };
    await auth.register(userData);
} catch (error) {
    console.error('Registration failed:', error);
}

// Login
try {
    const credentials = {
        username: 'user123',
        password: 'password123'
    };
    const response = await auth.login(credentials);
    console.log('Login successful:', response);
} catch (error) {
    console.error('Login failed:', error);
}

// Making authenticated requests
const authenticatedAxios = auth.getAuthenticatedAxios();
try {
    const response = await authenticatedAxios.get('/some-protected-endpoint');
    console.log('Protected data:', response.data);
} catch (error) {
    console.error('Request failed:', error);
}
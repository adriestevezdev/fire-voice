document.addEventListener('DOMContentLoaded', () => {
  const statusElement = document.getElementById('status');
  const testBtn = document.getElementById('testBtn');

  if (testBtn && statusElement) {
    testBtn.addEventListener('click', async () => {
      const statusContainer = statusElement.parentElement;
      const button = testBtn as HTMLButtonElement;
      
      // Reset classes and show testing state
      statusContainer?.classList.remove('success', 'error');
      statusContainer?.classList.add('testing');
      statusElement.textContent = 'Testing connection...';
      button.disabled = true;
      
      try {
        const response = await (window as any).electronAPI.ping();
        
        // Show success state
        statusContainer?.classList.remove('testing');
        statusContainer?.classList.add('success');
        statusElement.textContent = `✅ Connected - Response: ${response}`;
        
        // Reset to normal after 3 seconds
        setTimeout(() => {
          statusContainer?.classList.remove('success');
          statusElement.textContent = 'Ready';
        }, 3000);
        
      } catch (error) {
        // Show error state
        statusContainer?.classList.remove('testing');
        statusContainer?.classList.add('error');
        statusElement.textContent = '❌ Connection failed';
        
        // Reset to normal after 3 seconds
        setTimeout(() => {
          statusContainer?.classList.remove('error');
          statusElement.textContent = 'Ready';
        }, 3000);
      } finally {
        button.disabled = false;
      }
    });
  }
});
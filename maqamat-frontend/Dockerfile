# Use Node.js as the base image
FROM node:18-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory's content into the container
COPY . .

# Install dependencies
RUN npm install

# Build the React app
RUN npm run build

# Expose the port
EXPOSE 3000

# Serve the React app
CMD ["npm", "start"]

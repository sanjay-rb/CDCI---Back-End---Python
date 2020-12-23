node {

    // Clone the latest repo from the git....
    stage("Git Clone") {
        git branch: 'main', credentialsId: '2ba18c43-fb6f-402b-98ad-91664d4ceab5', url: 'https://github.com/sanjaysanju618/CDCI---Back-End---Python.git'
    }

    // Start building the python env into the docker container....
    stage("Build Python") {
        try {
            // Remove the old container if not running....
            bat 'docker container stop api'
            bat 'docker container rm api'
            bat 'docker image rm api'
        } catch(err) {
            bat 'echo Create new Python Image'
        } finally {
            bat 'docker build --tag api .'
        }
    }

    // Start the server or restart the server if running....
    stage("Start Server") {
        try {
            // Start the server on 5000 port....
            bat 'docker run -d -p 5000:5000 --name api api'
        } catch (err) {
            // Restart the server if it is running....
            bat 'docker container restart api'
        }
    }
}
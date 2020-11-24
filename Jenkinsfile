node {
    stage("Git Clone") {
        git branch: 'main', credentialsId: '2ba18c43-fb6f-402b-98ad-91664d4ceab5', url: 'https://github.com/sanjaysanju618/CDCI---Back-End---Python.git'
    }
    stage("Build Python") {
        try {
            bat 'docker container stop api'
            bat 'docker container rm api'
            bat 'docker image rm api'
        } catch(err) {
            bat 'echo Create new Python Image'
        } finally {
            bat 'docker build --tag api .'
        }
    }
    stage("Start Server") {
        try {
            bat 'docker run -d -p 5000:5000 --name api api'
        } catch (err) {
            bat 'docker container restart api'
        }
    }
}
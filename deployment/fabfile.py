from fabric.api import local
from fabric.api import lcd
from fabric.api import run
from fabric.api import put


# fab prepare:<your_branch_name>
# fab deploy


def hello():
    print("Hello world!")


def prepare(branch_name):
    #local('python manage.py test dashboard')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)


def test():
    local('python manage.py test dashboard')


def copy():
    # make sure the directory is there!
    run('mkdir -p C:\Server\mysite2')

    # our local 'localdirectory' (it may contain files or subdirectories)
    put('localdirectory', 'C:\Server\mysite2')



def deploy():
    with lcd('C:\Server\mysite2'):
        local('git pull D:\z_phytonprojects\decisionmanager_project\decisionmanager')
        local('python manage.py migrate dashboard')
        local('python manage.py test dashboard')
        #local('/my/command/to/restart/webserver')
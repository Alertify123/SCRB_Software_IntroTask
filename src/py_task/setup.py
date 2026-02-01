from setuptools import find_packages, setup

package_name = 'py_task'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chrisjan',
    maintainer_email='chrisjan.alejandro06@gmail.com',
    description='Intro task for minimal publisher/subscriber using rclpy',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'talker = py_task.task_publisher:main',
        'listener = py_task.task_subscriber:main',
        ],
    },
)

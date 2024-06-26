import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'amr_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tomascadete',
    maintainer_email='tomascadete@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'perception = amr_sim.perception:main',
            'tracker = amr_sim.tracker:main',
            'control = amr_sim.control:main',
            'planner = amr_sim.planner:main',
            'traffic_light_detection = amr_sim.traffic_light_detection:main',
            'trajectory_plotter = amr_sim.trajectory_plotter:main',
            'predictor = amr_sim.predictor:main'
        ],
    },
)

cmake_minimum_required(VERSION 3.16)
project(NeuralPhysicsEngine)

set(CMAKE_CXX_STANDARD 17)

# Engine core
add_subdirectory(src)

# Samples
add_executable(particles_demo samples/particles_demo.cpp)
target_link_libraries(particles_demo engine_core)

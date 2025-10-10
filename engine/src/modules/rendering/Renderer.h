#pragma once

#include <string>
#include <vector>
#include <glm/glm.hpp>

class Shader {
public:
    unsigned int ID;
    Shader(const std::string& vertexPath, const std::string& fragmentPath);
    void use() const;
    void setMat4(const std::string& name, const glm::mat4& mat) const;
    void setVec3(const std::string& name, const glm::vec3& value) const;
    void setFloat(const std::string& name, float value) const;
    // ... other uniform setters
};

struct Vertex {
    glm::vec3 Position;
    glm::vec3 Normal;
    glm::vec2 TexCoords;
};

struct Texture {
    unsigned int id;
    std::string type;
    std::string path;
};

class Mesh {
public:
    std::vector<Vertex> vertices;
    std::vector<unsigned int> indices;
    std::vector<Texture> textures;

    Mesh(const std::vector<Vertex>& vertices, const std::vector<unsigned int>& indices, const std::vector<Texture>& textures);
    void Draw(const Shader& shader) const;
private:
    unsigned int VAO, VBO, EBO;
    void setupMesh();
};

class Renderer {
public:
    Renderer();
    ~Renderer();
    void DrawMesh(const Mesh& mesh, const Shader& shader) const;
    Mesh LoadMesh(const std::string& path);
    Shader LoadShader(const std::string& vertexPath, const std::string& fragmentPath);
};
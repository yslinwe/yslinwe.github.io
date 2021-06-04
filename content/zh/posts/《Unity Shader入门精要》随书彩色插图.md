---
title: "《Unity Shader入门精要》随书彩色插图"
summary: Unity Shader入门精要
date: 2021-06-04
tags: ["Unity Shader入门精要"]
author: "冯乐乐"
draft: false
weight: 2
---

------

说明：本页面是书籍《Unity Shader入门精要》的随书彩图集锦，包含了书中所有的插图，使用时可通过图片编号进行搜索。
作者：冯乐乐
邮箱：lelefeng1992@gmail.com

------

### 前言



![shadertoy.png-286.5kB](http://static.zybuluo.com/candycat/x27bgzdj1cmfbzxa43z8t5qw/shadertoy.png)



### 第2章 渲染流水线




![流水线.png-83.4kB](http://static.zybuluo.com/candycat/zqt40itigpzl8qkn30m433g6/%E6%B5%81%E6%B0%B4%E7%BA%BF.png)
图2.1　真实生活中的流水线

![概念流水线.png-16.9kB](http://static.zybuluo.com/candycat/c0opg7bab4cwzyok5vek52hs/%E6%A6%82%E5%BF%B5%E6%B5%81%E6%B0%B4%E7%BA%BF.png)
图2.2 渲染流水线中的三个概念阶段

![CopyDataToGPU.png-86.5kB](http://static.zybuluo.com/candycat/qwr4r6aglmod38w2k1e0dq7h/CopyDataToGPU.png)
图2.3 渲染所需的数据（两张纹理以及3个网格）从硬盘最终加载到显存中。在渲染时，GPU可以快速访问这些数据

![SetRenderState.png-157.1kB](http://static.zybuluo.com/candycat/gld5mfj5o10kardzyn10p5a6/SetRenderState.png)
图2.4 在同一状态下渲染三个网格。由于没有更改渲染状态，因此三个网格的外观看起来像是同一种材质的物体。

![DrawCall.png-59.1kB](http://static.zybuluo.com/candycat/5nuo5d8oh1c8sxexr3d7e935/DrawCall.png)
图2.5 CPU通过调用Draw Call来告诉GPU开始进行一个渲染过程。一个Draw Call会指向本次调用需要渲染的图元列表

![GPU流水线.png-82.2kB](http://static.zybuluo.com/candycat/jundxsf604yuoy2zr3r1qkzp/GPU%E6%B5%81%E6%B0%B4%E7%BA%BF.png)
图2.6 GPU的渲染流水线实现。颜色表示了不同阶段的可配置性或可编程性：绿色表示该流水线阶段是完全可编程控制的，黄色表示该流水线阶段可以配置但不是可编程的，蓝色表示该流水线阶段是由GPU固定实现的，开发者没有任何控制权。实线表示该shader必须由开发者编程实现，虚线表示该Shader是可选的

![VertexShaderProcess.png-43kB](http://static.zybuluo.com/candycat/07rjqb1pkfipxiizr1nsywuf/VertexShaderProcess.png)
图2.7 GPU在每个输入的网格顶点上都会调用顶点着色器。顶点着色器必须进行顶点的坐标变换，需要时还可以计算和输出顶点的颜色。例如，我们可能需要进行逐顶点的光照

![Vertex Shader.png-34.9kB](http://static.zybuluo.com/candycat/2zpu3oh7n6kpy4rosqtjugcy/Vertex%20Shader.png)
图2.8 顶点着色器会将模型顶点的位置变换到齐次裁剪坐标空间下，进行输出后再由硬件做透视除法得到NDC下的坐标

![Clipping.png-25.5kB](http://static.zybuluo.com/candycat/08cvo0uahel9ygds4xkwrczp/Clipping.png)
图2.9 只有在单位立方体的图元才需要被继续处理。因此，完全在单位立方体外部的图元（红色三角形）被舍弃，完全在单位立方体内部的图元（绿色三角形）将被保留。和单位立方体相交的图元（黄色三角形）会被裁剪，新的顶点会被生成，原来在外部的顶点会被舍弃

![ScreenMapping.png-22.6kB](http://static.zybuluo.com/candycat/7xtfj07anrw60g4y7cadkd8h/ScreenMapping.png)
图2.10 屏幕映射将x、y坐标从（-1, 1）范围转换到屏幕坐标系中

![Screen Mapping_OpenGL_DirectX.png-26.9kB](http://static.zybuluo.com/candycat/ul58wnwn76vj0gm20m3xsi9g/Screen%20Mapping_OpenGL_DirectX.png)
图2.11 OpenGL和DirectX的屏幕坐标系差异。对于一张512*512大小的图像，在OpenGL中其（0, 0）点在左下角，而在DirectX中其(0, 0)点在左上角

![TriangleSetupAndTraversal.png-80kB](http://static.zybuluo.com/candycat/1ltkl388mkbbzbfgzm28f6gy/TriangleSetupAndTraversal.png)
图2.12 三角形遍历的过程。根据几何阶段输出的顶点信息，最终得到该三角网格覆盖的像素位置。对应像素会生成一个片元，而片元中的状态是对三个顶点的信息进行插值得到的。例如，对图2.12中三个顶点的深度进行插值得到其重心位置对应的片元的深度值为-10.0

![FragmentShader.png-42.4kB](http://static.zybuluo.com/candycat/lowfuoi0r43oxfgxkp9darur/FragmentShader.png)
图2.13 根据上一步插值后的片元信息，片元着色器计算该片元的输出颜色

![Per-fragment Operations.png-23.1kB](http://static.zybuluo.com/candycat/epejev04t6vudwsyo2el8rp0/Per-fragment%20Operations.png)
图2.14 逐片元操作阶段所做的操作。只有通过了所有的测试后，新生成的片元才能和颜色缓冲区中已经存在的像素颜色进行混合，最后再写入颜色缓冲区中

![Stencil Test_Depth Test.png-93.5kB](http://static.zybuluo.com/candycat/28t2ora2kenj1uudwfgfig95/Stencil%20Test_Depth%20Test.png)
图2.15 模板测试和深度测试的简化流程图。

![Blending.png-67.6kB](http://static.zybuluo.com/candycat/k7q79qcgoqkw8myu1lpuy7he/Blending.png)
图2.16 混合操作的简化流程图

![why_early_depth_test.png-18.7kB](http://static.zybuluo.com/candycat/kqngym2i5cvgo5bnkpfjabpi/why_early_depth_test.png)
图2.17 图示场景中包含了两个对象：球和长方体，绘制顺序是先绘制球（在屏幕上显示为圆），再绘制长方体（在屏幕上显示为长方形）。如果深度测试在片元着色器之后执行，那么在渲染长方体时，虽然它的大部分区域都被遮挡在球的后面，即它所覆盖的绝大部分片元根本无法通过深度测试，但是我们仍然需要对这些片元执行片元着色器，造成了很大的性能浪费

![OpenGL和DirectX.png-56.1kB](http://static.zybuluo.com/candycat/4x54y4f2kjlhil8wq7oi1fpa/OpenGL%E5%92%8CDirectX.png)
图2.18 CPU、OpenGL/DirectX、显卡驱动和GPU之间的关系

![CommandBuffer.png-49.9kB](http://static.zybuluo.com/candycat/h9oh7t35lbjrgogxywarmu55/CommandBuffer.png)
图2.19 命令缓冲区。CPU通过图像编程接口向命令缓冲区中添加命令，而GPU从中读取命令并执行。黄色方框内的命令就是Draw Call，而红色方框内的命令用于改变渲染状态。我们使用红色方框来表示改变渲染状态的命令， 是因为这些命令往往更加耗时

![SmallCommand.png-107.7kB](http://static.zybuluo.com/candycat/pef7ujj1xdzmzwdwz3n261rz/SmallCommand.png)
图2.20 命令缓冲区中的虚线方框表示GPU已经完成的命令。此时，命令缓冲区中没有可以执行的命令了，GPU处于空闲状态，而CPU还没有准备好下一个渲染命令。

![Batching.png-70.3kB](http://static.zybuluo.com/candycat/d6cxj75dc7hnzwd2jlcqlj4j/Batching.png)
图2.21 利用批处理，CPU在RAM把多个网格合并成一个更大的网格，再发送给GPU，然后在一个Draw Call中渲染它们。但要注意的是，使用批处理合并的网格将会使用同一种渲染状态。也就是说，如果网格之间需要使用不同的渲染状态，那么就无法使用批处理技术







### 第3章 Unity Shader基础





![material_shader.png-125.8kB](http://static.zybuluo.com/candycat/hojqrwubqu22k9jo0ues60hd/material_shader.png)
图3.1 Unity Shader和材质。首先创建需要的Unity Shader和材质，然后把Unity Shader赋给材质，并在材质面板上调整属性（如使用的纹理、漫反射系数等）。最后，将材质赋给相应的模型来查看最终的渲染效果

![mesh_renderer.png-41kB](http://static.zybuluo.com/candycat/fupmmv6n7raqei37v4jj6su1/mesh_renderer.png)
图3.2 将材质直接拖曳到模型的Mesh Renderer组件中

![material_inspector.png-119.4kB](http://static.zybuluo.com/candycat/936v924ooiux4x9v9l6nw7w2/material_inspector.png)
图3.3 材质提供了一种可视化的方式来调整着色器中使用的参数

![shader_import_settings.png-38kB](http://static.zybuluo.com/candycat/dwq288k4s50acnc7sx2wz9fp/shader_import_settings.png)
图3.4 Unity Shader的导入设置面板

![shader_compile_code.png-35.9kB](http://static.zybuluo.com/candycat/wvudje920on69gto9p9jq6bo/shader_compile_code.png)
图3.5 Gompile and show code下拉列表

![shaderlab_abstract.png-63.4kB](http://static.zybuluo.com/candycat/mfyfmiwipc220l4v8iowww6k/shaderlab_abstract.png)
图3.6 Unity Shader为控制渲染过程提供了一层抽象。如果没有使用Unity Shader（左图），开发者需要和很多文件和设置打交道，才能让画面呈现出想要的效果；而在Unity Shader的帮助下（右图），开发者只需要使用ShaderLab来编写Unity Shader文件就可以完成所有的工作

![shader_name.png-55.5kB](http://static.zybuluo.com/candycat/7u7q53pfa4pbtapi9wz9b6f7/shader_name.png)
图3.7 在Unity Shader的名称定义中利用 斜杠来组织在材质面板中的位置

![shaderlab_properties.png-33.2kB](http://static.zybuluo.com/candycat/izzjwk3okp3r41uok617ry8t/shaderlab_properties.png)
图3.8 不同属性类型在材质 面板中的显示结果

![shader_compile_code.png-35.9kB](http://static.zybuluo.com/candycat/55s9cmdps9zqm738ls4ibuho/shader_compile_code.png)
图3.9 在Unity Shader的导入设置面板中可以通过Compile and show code按钮来查看Unity对CG片段编译后的代码。通过单击Compile and show code按钮右端的倒三角可以打开下拉菜单，在这个下拉菜单中可以选择编译的平台种类，如只为当前的显卡设备编译特定的汇编代码，或为所有的平台编译汇编代码，我们也可以自定义选择编译到哪些平台上





### 第4章 学习Shader所需的数学基础





![little_cow.png-293.5kB](http://static.zybuluo.com/candycat/tdhtbh0rhx1dw94fbegmfxg9/little_cow.png)
图4.1 我们的农场游戏。我们的主角妞妞是一头长得最壮、好奇心很强的奶牛

![cartersian_fly.png-28kB](http://static.zybuluo.com/candycat/u6pb6kylub8zxfwxotxs3cbm/cartersian_fly.png)
图4.2 传说，笛卡尔坐标系来源于笛卡尔对天花板上一只苍蝇的运动轨迹的观察。笛卡尔发现，可以使用苍蝇距不同墙面的距离来描述它的当前位置

![2d_cartesian.png-36.4kB](http://static.zybuluo.com/candycat/in4byrrfu29pr19hhfmzaqsw/2d_cartesian.png)
图4.3 一个二维笛卡尔坐标系

![2d_cartesian_opengl_directx.png-33.1kB](http://static.zybuluo.com/candycat/s4twn4lnbvlac7ci3mwwbe4d/2d_cartesian_opengl_directx.png)
图4.4 在屏幕映射时，OpenGL和DirectX使用了不同方向的二维笛卡尔坐标系

![cow_cartesian.png-211.8kB](http://static.zybuluo.com/candycat/9n615pcahnqo38xx5dm8vxpi/cow_cartesian.png)
图4.5 笛卡尔坐标系可以让妞妞精确表述自己的位置

![3d_cartesian.png-22.7kB](http://static.zybuluo.com/candycat/tp39jr06yzo8u4gdzp0z1qqs/3d_cartesian.png)
图4.6 一个三维笛卡尔坐标系

![left_hand.png-40.5kB](http://static.zybuluo.com/candycat/7vdjcritmzv94yosp538yq7w/left_hand.png)
图4.7 左手坐标系

![right_hand.png-40kB](http://static.zybuluo.com/candycat/5llpe09e7f8mtdu7h49s88r1/right_hand.png)
图4.8 右手坐标系

![left_right_hand_rule.png-75.3kB](http://static.zybuluo.com/candycat/w5i9lq84fphxch5x8tjtzqo2/left_right_hand_rule.png)
图4.9 用左手法则和右手法则来判断旋转正方向

![cow_left_right.png-254.3kB](http://static.zybuluo.com/candycat/i65z04v7mbcufxsjkx7n0n67/cow_left_right.png)
图4.10 为了移动到新的位置，妞妞需要首先向某个方向平移1个单位，再向另一个方向平移4个单位，最后再向一个方向旋转60°

![cow_left_right_hand.png-295.8kB](http://static.zybuluo.com/candycat/janos0r95h321yeoeufigdog/cow_left_right_hand.png)
图4.11 左图和右图分别表示了在左手坐标系和右手坐标系中描述妞妞这次运动的结果，得到的数学描述是不同的

![unity_cartesian.png-173.2kB](http://static.zybuluo.com/candycat/7xx63gosl0504rj16wdcnare/unity_cartesian.png)
图4.12 在模型空间和世界空间中，Unity使用的是左手坐标系。图中，球的坐标轴显示了它在模型空间中的3个坐标轴（红色为x轴，绿色是y轴，蓝色是z轴）

![unity_camera_cartesian.png-25.1kB](http://static.zybuluo.com/candycat/lrhkf34n8p5fz7mzyro7r72m/unity_camera_cartesian.png)
图4.13 在Unity中，观察空间使用的是右手坐标系，摄像机的前向是z轴的负方向， z轴越小，物体的深度越大，离摄像机越远

![exercise_3.png-130.8kB](http://static.zybuluo.com/candycat/t5slprvqvmndc1yve7x0lquo/exercise_3.png)
图4.14 摄像机的位置是（0, 1, -10），球体的位置是（0, 1, 0）

![vector.png-8.9kB](http://static.zybuluo.com/candycat/8e49l43g2xhp9wfs6r526226/vector.png)
图4.15 一个二维向量以及它的头和尾

![point_vector.png-16.1kB](http://static.zybuluo.com/candycat/jwojplbtid4z6xiuw7dso9t0/point_vector.png)
图4.16 点和矢量之间的关系

![vector_scalar.png-53.9kB](http://static.zybuluo.com/candycat/py5slc3wo9v78lpb25xcdas0/vector_scalar.png)
图4.17 二维矢量和一些标量的乘法和除法

![vector_add_sub.png-52.8kB](http://static.zybuluo.com/candycat/2y7rr3t5j8bct6ocnlvpydp6/vector_add_sub.png)
图4.18 二维矢量的加法和减法

![vector_displacement.png-22.5kB](http://static.zybuluo.com/candycat/051rzkws7n2ii9wep4b04t8f/vector_displacement.png)
图4.19 使用矢量减法来计算从点a到点b的位移

![vector_magnitude.png-8.2kB](http://static.zybuluo.com/candycat/lk35xmttonr0qliblc5v5lpu/vector_magnitude.png)
图4.20 矢量的模

![unit_vector.png-30.7kB](http://static.zybuluo.com/candycat/mqfl49yeebwbqtc23i755qux/unit_vector.png)
图4.21 二维空间的单位矢量都会落在单位圆上

![projection.png-17.7kB](http://static.zybuluo.com/candycat/rlo1hwsdb334yi9i9vimdtko/projection.png)
图4.22 矢量b在单位矢量a方向上的投影

![dot_sign.png-22.9kB](http://static.zybuluo.com/candycat/wet7zoq1bssb0u8gm63zfmx6/dot_sign.png)
图4.23 点积的符号

![dot_cos.png-14.1kB](http://static.zybuluo.com/candycat/xnouckzvbcb59nqcanijjpx7/dot_cos.png)
图4.24 两个单位矢量进行点积

![vector_cross_diagram.png-32.1kB](http://static.zybuluo.com/candycat/yrl5ol849v5h8892l4bqlgrh/vector_cross_diagram.png)
图4.25 三维矢量叉积的计算规律。不同颜色的线表示了计算结果矢量中对应颜色的分量的计算路径。以红色为例，即结果矢量的第一个分量，它是从第一个矢量的y分量出发乘以第二个矢量的z分量，再减去第一个矢量的z分量和第二矢量的y分量的乘积

![vector_cross_length.png-13kB](http://static.zybuluo.com/candycat/fh9vcn0q1g5te175pqg9beu3/vector_cross_length.png)
图4.26 使用矢量a和矢量b构建一个平行四边形

![vector_cross.png-27.2kB](http://static.zybuluo.com/candycat/0d3l6dqc7q6d3h6vxkqjqo99/vector_cross.png)
图4.27 分别使用左手坐标系和右手坐标系得到的叉积结果

![vector_cross_right_hand.png-46.6kB](http://static.zybuluo.com/candycat/t6i0a60k7rd05a5url0wljcl/vector_cross_right_hand.png)
图4.28 使用右手法则判断右手坐标系中a×b的方向

![exercise_cross.png-26.1kB](http://static.zybuluo.com/candycat/5oy7iqjnkyi69v1d2sayhxf0/exercise_cross.png)
图4.29 三角形的三个顶点位于xy平面上，人眼位于z轴负方向，向z轴正方向观察

![matrix_mul.png-25kB](http://static.zybuluo.com/candycat/u6urub3wacveq0qcr6112we5/matrix_mul.png)
图4.30 计算c23的过程

![niuniu.png-273.2kB](http://static.zybuluo.com/candycat/ncg6g1ragp0bfufbm2m3ir2m/niuniu.png)
图4.31 场景中的妞妞（左图）和屏幕上的妞妞（右图）。妞妞想知道，自己的鼻子是如何被画到屏幕上的

![object_space.png-84.5kB](http://static.zybuluo.com/candycat/o85jqc1fw9rt10f0n485y9vt/object_space.png)
图4.32 在我们的农场游戏中，每个奶牛都有自己的模型坐标系。在模型坐标系中妞妞鼻子的位置是(0, 2, 4, 1)

![unity_transform.png-151.9kB](http://static.zybuluo.com/candycat/drp1660u59nwnw8d2hvb0rrg/unity_transform.png)
图4.33 Unity的Transform组件可以调节模型的位置.如果Transform有父节点，如图中的“Mesh”，那么Position将是在其父节点（这里是“Cow”）的模型空间中的位置；如果没有父节点，Position就是在世界空间中的位置

![world_space.png-378.7kB](http://static.zybuluo.com/candycat/ozup3egxnxqp21otm4z6jzhx/world_space.png)
图4.34 农场游戏中的世界空间。世界空间的原点被放置在农场的中心。左下角显示了妞妞在世界空间中所做的变换。我们想要把妞妞的鼻子从模型空间变换到世界空间中

![camera_space.png-346.2kB](http://static.zybuluo.com/candycat/8q0v8m4wwkm2h9homadyeear/camera_space.png)
图4.35 农场游戏中摄像机的观察空间。观察空间的原点位于摄像机处。注意在观察空间中，摄像机的前向是z轴的负方向（图中只画出了z轴正方向），这是因为Unity在观察空间中使用了右手坐标系。左下角显示了摄像机在世界空间中所做的变换。我们想要把妞妞的鼻子从世界空间变换到观察空间中

![camera_projection.png-299.3kB](http://static.zybuluo.com/candycat/wqkekwazaaordawbq21nj7hz/camera_projection.png)
图4.36 透视投影（左图）和正交投影（右图）。左下角分别显示了当前摄像机的投影模式和相关属性

![camera_frustum.png-301.2kB](http://static.zybuluo.com/candycat/b6wiym3nlkwimvnvgjgohhbz/camera_frustum.png)
图4.37 视锥体和裁剪平面。左图显示了透视投影的视锥体，右图显示了正交投影的视锥体

![projection_frustum.png-67.3kB](http://static.zybuluo.com/candycat/j6w23tgb5a1acjq6mr73ietq/projection_frustum.png)
图4.38 透视摄像机的参数对透视投影视锥体的影响

![projection_matrix0.png-135.1kB](http://static.zybuluo.com/candycat/tddwy4107pnswnbxydxc2rsp/projection_matrix0.png)
图4.39 在透视投影中，投影矩阵对顶点进行了缩放。图3.38中标注了4个关键点经过投影矩阵变换后的结果。从这些结果可以看出x、y、z和w分量的范围发生的变化

![orthographic_frustum.png-33.5kB](http://static.zybuluo.com/candycat/0r3xdlarpzqf94nfb304qihx/orthographic_frustum.png)
图4.40 正交摄像机的参数对正交投影视锥体的影响

![orthographic_matrix0.png-129.6kB](http://static.zybuluo.com/candycat/2j2ea1iexjim88y8towjkjlz/orthographic_matrix0.png)
图4.41 在正交投影中，投影矩阵对顶点进行了缩放。图中标注了4个关键点经过投影矩阵变换后的结果。从这些结果可以看出x、y、z和w分量范围发生的变化

![cow_camera.png-180.1kB](http://static.zybuluo.com/candycat/si6bqxafh76xku3i0bxp91lq/cow_camera.png)
图4.42 农场游戏使用的摄像机参数和游戏画面的横纵比

![projection_matrix1.png-131kB](http://static.zybuluo.com/candycat/7ozeba0c8nex3o4zr9z9nt4v/projection_matrix1.png)
图4.43 经过齐次除法后，透视投影的裁剪空间会变换到一个立方体

![orthographic_matrix1.png-105.6kB](http://static.zybuluo.com/candycat/8921u8zbn1m38conxbed0nz5/orthographic_matrix1.png)
图4.44 经过齐次除法后，正交投影的裁剪空间会变换到一个立方体

![vertex_conversion.png-100.9kB](http://static.zybuluo.com/candycat/z0ibvp779phr1hb0l902n1qy/vertex_conversion.png)
图4.45 渲染流水线中顶点的空间变换过程

![space_handness.png-75.6kB](http://static.zybuluo.com/candycat/jxcomxjmrye6rczmlyw550wt/space_handness.png)
图4.46 Unity中各个坐标空间的旋向性

![normal_tangent.png-167.3kB](http://static.zybuluo.com/candycat/cjevn0tuacb13ssus1sj8ceo/normal_tangent.png)
图4.47 顶点的切线和法线。切线和法线互相垂直

![transform_normal.png-40.6kB](http://static.zybuluo.com/candycat/80ofuzudfjzrrl8r1gcxinse/transform_normal.png)
图4.48 进行非统一缩放时，如果使用和变换顶点相同的变换矩阵来变换法线，就会得到错误的结果，即变换后的法线方向与平面不再垂直

![screen_coord.png-9kB](http://static.zybuluo.com/candycat/9puxwch79e92gzv5xfrsh3qm/screen_coord.png)
图4.49 由片元的像素位置得到的图像

![difference_between_left_right.png-54.6kB](http://static.zybuluo.com/candycat/zvcl27rgm897ir8w18m1bii2/difference_between_left_right.png)
图4.50 图中两个坐标系的x轴和y轴是重合的，区别仅在于z轴的方向。左手坐标系的（0, 0, 1）点和右手坐标系中的（0, 0, 1）点是不同的，但它们旋转后的点却对应到了同一点

![difference_between_left_right_2.png-59.4kB](http://static.zybuluo.com/candycat/akhas8nqu68ps3rd1kuhi0hf/difference_between_left_right_2.png)
图4.51 绝对空间中的同一点，在左手和右手坐标系中进行同样角度的旋转，其旋转方向是不一样的。在左手坐标系中将按顺时针方向旋转，在右手坐标系中将按逆时针方向旋转

![exercise_cross2.png-34.4kB](http://static.zybuluo.com/candycat/tw8il4lajuaf6dxx7l0yj9zd/exercise_cross2.png)
图4.52 在左手坐标系中，如果叉积结果为负，那么3点的顺序是顺时针方向





### 第5章 开始Unity Shader学习之旅





![new_scene.png-74.3kB](http://static.zybuluo.com/candycat/9b4lok82evuyq772bhbnnl6x/new_scene.png)
图5.1 在Unity 5中新建一个场景得到的效果

![simple_shader.png-25.4kB](http://static.zybuluo.com/candycat/4se9aphevcooho5wm1bsqxm0/simple_shader.png)
图5.2 用一个最简单的顶点/片元着色器得到一个白色的球

![cginclude.png-27kB](http://static.zybuluo.com/candycat/umffe4syp5ttjtilp9ydyd2k/cginclude.png)
图5.3 Unity的内置着色器

![false_color.png-192.9kB](http://static.zybuluo.com/candycat/yao0f655aycbk2kehmleei2p/false_color.png)
图5.4 用假彩色对Unity Shader进行调试

![color_picker.png-53.8kB](http://static.zybuluo.com/candycat/tx3a01nq92yshsc1y72n6s4j/color_picker.png)
图5.5 使用颜色拾取器来查看调试信息

![frame_debugger.png-218.7kB](http://static.zybuluo.com/candycat/dx8svpr4bxtegcns8e50lgf6/frame_debugger.png)
图5.6 帧调试器

![frame_debugger_0.png-164.5kB](http://static.zybuluo.com/candycat/11gb131ywty31xni4smc77ol/frame_debugger_0.png)
图5.7 单击Knot的深度图渲染事件，在Game视图会显示该事件的效果，在Hierarchy视图中会高亮显示Knot对象，在帧调试器的右侧窗口会显示出该事件的细节

![2d_cartesian_opengl_directx.png-33.1kB](http://static.zybuluo.com/candycat/ninmtxykcrk7oywzvxirhn04/2d_cartesian_opengl_directx.png)
图5.8 OpenGL和DirectX使用了不同的屏幕空间坐标





### 第6章 Unity中的基础光照





![irradiance.png-60.3kB](http://static.zybuluo.com/candycat/tzgu5oq816ojbkjo4y05rvij/irradiance.png)
图6.1 在左图中，光是垂直照射到物体表面，因此光线之间的垂直距离保持不变；而在右图中，光是斜着照射到物体表面，在物体表面光线之间的距离是d/cosθ，因此单位面积上接收到的光线数目要少于左图

![scattering.png-37.1kB](http://static.zybuluo.com/candycat/7gu6p5xdmzngz53iaa011joy/scattering.png)
图6.2 散射时，光线会发生折射和反射现象。对于不透明物体，折射的光线会在物体内部继续传播，最终有一部分光线会重新从物体表面被发射出去

![specular.png-31.2kB](http://static.zybuluo.com/candycat/51iph9ayl3l22w3xuzeumwxf/specular.png)
图6.3 使用Phong模型计算高光反射

![Blinn.png-32.1kB](http://static.zybuluo.com/candycat/nntler7jilkso6zufrbw447c/Blinn.png)
图6.4 Blinn模型

![ambient.png-35.3kB](http://static.zybuluo.com/candycat/4pgo8idyb8gsjlq5xbynoj8d/ambient.png)
图6.5 在Unity的Window -> Lighting面板中，我们可以通过Ambient Source/Ambient Color/Ambient Intensity来控制场景中的环境光的颜色和强度

![diffuse_vertex_level.png-40.4kB](http://static.zybuluo.com/candycat/tow3hbf8of391rb7sumri3sy/diffuse_vertex_level.png)
图6.6 逐顶点的漫反射光照效果

![diffuse_pixel_level.png-40.1kB](http://static.zybuluo.com/candycat/6vlfiln2hnmhndp3m5uma9bs/diffuse_pixel_level.png)
图6.7 逐像素的漫反射光照效果

![diffuse_compare_all.png-86.9kB](http://static.zybuluo.com/candycat/kc9sg9dsvf7i23my26yii8gt/diffuse_compare_all.png)
图6.8 逐顶点漫反射光照、逐像素漫反射光照、半兰伯特光照的对比效果

![reflect.png-9.2kB](http://static.zybuluo.com/candycat/zldeemd0807hp485mkgp6qkr/reflect.png)
图6.9 CG的reflect函数

![specular_vertex_level.png-41.5kB](http://static.zybuluo.com/candycat/zw9y4jmxj7pivjakhb2tjcnm/specular_vertex_level.png)
图6.10 逐顶点的高光反射光照效果

![specular_pixel_level.png-40.8kB](http://static.zybuluo.com/candycat/ze75kza2bpckowcdfcuqsqx6/specular_pixel_level.png)
图6.11 逐像素的高光反射光照效果

![specular_compare_all.png-82.5kB](http://static.zybuluo.com/candycat/5d2r1xz062iykspwapu0txq1/specular_compare_all.png)
图6.12 逐顶点的高光反射光照、逐像素的高光反射光照（Phong光照模型）和Blinn-Phong高光反射光照的对比结果





### 第7章 基础纹理





![texture_coordinate.png-349.3kB](http://static.zybuluo.com/candycat/rcl2u5im3ef0pb1esf4pvz06/texture_coordinate.png)
图7.1 Unity中的纹理坐标

![single_texture.png-71.3kB](http://static.zybuluo.com/candycat/90xmbvepdh5lywclqutr989j/single_texture.png)
图7.2 使用单张纹理

![texture_tiling_offset.png-16.9kB](http://static.zybuluo.com/candycat/p60yfqpxafslgw0b8m3t2vd6/texture_tiling_offset.png)
图7.3 调节纹理的平铺（缩放）和偏移（平移）属性

![texture_properties.png-29kB](http://static.zybuluo.com/candycat/nfnonexamcr821gvsqfwm0rc/texture_properties.png)
图7.4 纹理的属性

![wrap_mode.png-68.9kB](http://static.zybuluo.com/candycat/fs3ikv46cf3h1rumombx5toy/wrap_mode.png)
图7.5 Wrap Mode决定了当纹理坐标超过[0, 1]范围后将会如何被平铺

![texture_offset.png-68.4kB](http://static.zybuluo.com/candycat/3pu5fg044fhfd9zcvhmx1mue/texture_offset.png)
图7.6 偏移（Offset）属性决定了纹理坐标的偏移量

![magnification.png-256.2kB](http://static.zybuluo.com/candycat/e15n8gjm48ldr8eoavr7p7k1/magnification.png)
图7.7 在放大纹理时，分别使用三种Filter Mode得到的结果

![mipmap.png-35.9kB](http://static.zybuluo.com/candycat/jtlnp9o3hnkv4sapauejzudg/mipmap.png)
图7.8 在Advanced模式下可以设置多级渐远纹理的相关属性

![minification.png-271.9kB](http://static.zybuluo.com/candycat/jphpd33ux984u48qtrebzb93/minification.png)
图7.9 从上到下： Point滤波 + 多级渐远纹理技术，Bilinear滤波 + 多级渐远纹理技术，Trilinear滤波 + 多级渐远纹理技术

![texture_quality.png-31.7kB](http://static.zybuluo.com/candycat/3tqq3cu9wdo0z874ukzje19h/texture_quality.png)
图7.10 选择纹理的最大尺寸和纹理模式

![heightmap.png-134.5kB](http://static.zybuluo.com/candycat/679mbns3qqorjgdlzjd9f64w/heightmap.png)
图7.11 高度图

![tangent_space.png-165.3kB](http://static.zybuluo.com/candycat/fpgdxhkx2vrfag4wpxkubh08/tangent_space.png)
图7.12 模型顶点的切线空间。其中，原点对应了顶点坐标，x轴是切线方向（t），y轴是副切线方向（b），z轴是法线方向（n）

![object_tangent_space_normal.png-320.3kB](http://static.zybuluo.com/candycat/cn4bj1pud3ttm5mrlfa4l891/object_tangent_space_normal.png)
图7.13 左图：模型空间下的法线纹理。右图：切线空间下的法线纹理

![normal_map.png-92.2kB](http://static.zybuluo.com/candycat/xwv6ca3g9fdhlnu1a48lw1o4/normal_map.png)
图7.14 使用法线纹理

![bump_scale.png-140.5kB](http://static.zybuluo.com/candycat/ewkjgj08b94xafdzgroq7wgh/bump_scale.png)
图7.15 使用Bump Scale属性来调整模型的凹凸程度

![texture_type_normal.png-29.8kB](http://static.zybuluo.com/candycat/98ol95g0rx90mbdan3fiw4n7/texture_type_normal.png)
图7.16 当使用UnpackNormal函数计算法线纹理中的法线方向时，需要把纹理类型标识为Normal map

![texture_type_heightmap.png-293.4kB](http://static.zybuluo.com/candycat/nd93fm3dgv4obtkxjo6dg2sg/texture_type_heightmap.png)
图7.17 当勾选了Create from Grayscale后，Unity会根据高度图来生成一张切线空间下的法线纹理

![ramp_texture.png-119.2kB](http://static.zybuluo.com/candycat/lqani27ay2sk4r52hgvz7fx1/ramp_texture.png)
图7.18 使用不同的渐变纹理控制漫反射光照，左下角给出了每张图使用的渐变纹理

![ramp_texture_wrap_mode.png-114.2kB](http://static.zybuluo.com/candycat/0wnw5wpwv2stmazzurh32jpt/ramp_texture_wrap_mode.png)
图7.19 Wrap Mode分别为Repeat和Clamp模式的效果对比

![mask_specular.png-142.4kB](http://static.zybuluo.com/candycat/h82ljkimcijox5hwj7ftpymy/mask_specular.png)
图7.20 使用高光遮罩纹理。从左到右：只包含漫反射，未使用遮罩的高光反射，使用遮罩的高光反射

![mask.png-671.4kB](http://static.zybuluo.com/candycat/bu4eyurnenwal307dwbhzp2r/mask.png)
图7.21 本节使用的高光遮罩纹理





### 第8章 透明效果





![render_order_0.png-10.7kB](http://static.zybuluo.com/candycat/48l0aapqc57v0gn367tk2akx/render_order_0.png)
图8.1 场景中有两个物体，其中A（黄色）是半透明物体，B（紫色）是不透明物体

![render_order_1.png-10.5kB](http://static.zybuluo.com/candycat/5k524ddo8qib31j6s4mhkekh/render_order_1.png)
图8.2 场景中有两个物体，其中A和B都是半透明物体

![render_order_3.png-15.3kB](http://static.zybuluo.com/candycat/sl85989h54upaju75zstyv0y/render_order_3.png)
图8.3 循环重叠的半透明物体总是无法得到正确的半透明效果

![render_order_2.png-30.4kB](http://static.zybuluo.com/candycat/hi3bbsss5t48uvmi83uzjle8/render_order_2.png)
图8.4 使用哪个深度对物体进行排序。红色点分别标明了网格上距离摄像机最近的点、最远的点以及网格中点

![transparent_texture.png-71.9kB](http://static.zybuluo.com/candycat/fq123k86x5alcbccjmv7gogl/transparent_texture.png)
图8.5 一张透明纹理，其中每个方格的透明度都不同

![alpha_test.png-55.9kB](http://static.zybuluo.com/candycat/w3n0yyn3rfwc0wv4dw7i02d2/alpha_test.png)
图8.6 透明度测试

![alpha_test_0.png-166.4kB](http://static.zybuluo.com/candycat/a4hmfr1eltd6shzthle7ed5q/alpha_test_0.png)
图8.7 随着Alpha cutoff参数的增大，更多的像素由于不满足透明度测试条件而被剔除

![alpha_blend.png-55.1kB](http://static.zybuluo.com/candycat/0voinls84at3n3mg77a13tdu/alpha_blend.png)
图8.8 透明度混合

![alpha_blend_0.png-138.7kB](http://static.zybuluo.com/candycat/5a1af3bgca3z399huyud2kwr/alpha_blend_0.png)
图8.9 随着Alpha Scale参数的增大，模型变得越来越透明

![transparent_order_wrong.png-94.7kB](http://static.zybuluo.com/candycat/4thev7v5xczq02bz824witrf/transparent_order_wrong.png)
图8.10 当模型网格之间有互相交叉的结构时，往往会得到错误的半透明效果

![alpha_blend_zwrite.png-87.9kB](http://static.zybuluo.com/candycat/1vknx9ilky82q0kmqnxns8aj/alpha_blend_zwrite.png)
图8.11 开启了深度写入的半透明效果

![blend.png-74.1kB](http://static.zybuluo.com/candycat/uvoq8qpet472e7fquzdu479t/blend.png)
图8.12 不同混合状态设置得到的效果

![alpha_test_both_sided.png-60.7kB](http://static.zybuluo.com/candycat/zcu57h732mubbea9ib45wx9u/alpha_test_both_sided.png)
图8.13 双面渲染的透明度测试的物体

![alpha_blend_both_sided.png-66.2kB](http://static.zybuluo.com/candycat/4tq24631e9aug7xswikf9awc/alpha_blend_both_sided.png)
图8.14 双面渲染的透明度混合的物体





### 第9章 更复杂的光照





![rendering_path_setting.png-30kB](http://static.zybuluo.com/candycat/n67qqzd3bc0q3gca2heih70h/rendering_path_setting.png)
图9.1 设置Unity项目的渲染路径

![rendering_path_camera.png-37.8kB](http://static.zybuluo.com/candycat/7wi9c0vibxtig4s1r45bugri/rendering_path_camera.png)
图9.2 摄像机组件的Rendering Path中的设置可以覆盖Project Settings中的设置

![light_type_mode.png-30.6kB](http://static.zybuluo.com/candycat/skolpwg0h7zzcey4gtl1rvc9/light_type_mode.png)
图9.3 设置光源的类型和渲染模式

![forward_rendering.png-175.5kB](http://static.zybuluo.com/candycat/575lq2zgnsaop3nw2miyobt3/forward_rendering.png)
图9.4 前向渲染的两种Pass

![directional_ligth.png-51.6kB](http://static.zybuluo.com/candycat/uadla1q69533nc71z7g7ep0g/directional_ligth.png)
图9.5 平行光

![point_ligtht.png-89.4kB](http://static.zybuluo.com/candycat/tvbpd08wgc0s1o31v4nw20ad/point_ligtht.png)
图9.6 点光源

![enable_light.png-63.6kB](http://static.zybuluo.com/candycat/8cpddt5rwnxg6ox6bml57ld7/enable_light.png)
图9.7 开启Scene视图中的光照

![spot_light.png-74.5kB](http://static.zybuluo.com/candycat/tx45g2n04xypq5cdlyblecrv/spot_light.png)
图9.8 聚光灯

![two_lights.png-79.4kB](http://static.zybuluo.com/candycat/bz1q9kyglm17psychsn255aq/two_lights.png)
图9.9 使用一个平行光和一个点光源共同照亮物体。右图显示了胶囊体、平行光和点光源在场景中的相对位置

![multi_lights.png-56.6kB](http://static.zybuluo.com/candycat/z4lor2cgc0gh8rwfjimk0ckq/multi_lights.png)
图9.10 使用1个平行光 + 4个点光源照亮一个物体

![frame_debugger.png-103.3kB](http://static.zybuluo.com/candycat/78c7qwpppd0h5baure1l9t1q/frame_debugger.png)
图9.11 打开帧调试器查看场景的绘制事件

![multi_lights_0.png-218.4kB](http://static.zybuluo.com/candycat/e4ruexwdln51zl9nrj8s6yrl/multi_lights_0.png)
图9.12 本例中的6个渲染事件，绘制顺序是从左到右、从上到下进行的

![multi_lights_1.png-100.8kB](http://static.zybuluo.com/candycat/d1wgzjrprligehvkdmq23pra/multi_lights_1.png)
图9.13 如果物体不在一个光源的光照范围内（从右图可以看出，胶囊体不在最左方的点光源的照明范围内），Unity是不会调用Additional Pass来为该物体处理该光源的

![light_not_important.png-70.8kB](http://static.zybuluo.com/candycat/joseae4o6388culiwx8tfntf/light_not_important.png)
图9.14 当把光源的Render Mode设为Not Important时，这些光源就不会按逐像素光来处理

![light_shadow.png-32.8kB](http://static.zybuluo.com/candycat/11n30be5vio56i8a35qdqzrd/light_shadow.png)
图9.15 开启光源的阴影效果

![mesh_renderer.png-20.3kB](http://static.zybuluo.com/candycat/tp559yfnp82fb3i5g5y5qc77/mesh_renderer.png)
图9.16 Mesh Renderer组件的Cast Shadows和Receive Shadows属性可以控制该物体是否投射/接收阴影

![shadow_0.png-34.4kB](http://static.zybuluo.com/candycat/rd60ljcaza6xcthui0q98m29/shadow_0.png)
图9.17 开启Cast Shadows和Receive Shadows，从而让正方体可以投射和接收阴影

![shadow_1.png-89kB](http://static.zybuluo.com/candycat/3t7vthpva2llk7madax2rcqs/shadow_1.png)
图9.18 把Cast Shadows设置为Two Sided可以让右侧平面的背光面也产生阴影

![shadow_2.png-40.5kB](http://static.zybuluo.com/candycat/d33yusj8nxye922idu6ws2xe/shadow_2.png)
图9.19 正方体可以接收来自右侧平面的阴影

![shadow_frame_debugger.png-81.6kB](http://static.zybuluo.com/candycat/3sjunj4mk8gizha7fve184m4/shadow_frame_debugger.png)
图9.20 使用帧调试器查看阴影绘制过程

![shadow_frame_debugger_0.png-83.1kB](http://static.zybuluo.com/candycat/c3c1kldvrbicscs1opg7ihjn/shadow_frame_debugger_0.png)
图9.21 正方体对深度纹理的更新结果

![shadow_frame_debugger_1.png-88.6kB](http://static.zybuluo.com/candycat/88mxjbzlwzyxsbncd8337dd1/shadow_frame_debugger_1.png)
图9.22 屏幕空间的阴影图

![shadow_frame_debugger_2.png-175.1kB](http://static.zybuluo.com/candycat/fv1abzu7knq289amxegwxqki/shadow_frame_debugger_2.png)
图9.23 Unity绘制屏幕阴影的过程

![alpha_test_shadow_0.png-62.8kB](http://static.zybuluo.com/candycat/v0wel6w64l5x0intcrfp3vdt/alpha_test_shadow_0.png)
图9.24 可以投射阴影的使用透明度测试的物体

![alpha_test_shadow_1.png-66.2kB](http://static.zybuluo.com/candycat/ap18z7090krmbw2ftx2u3e6z/alpha_test_shadow_1.png)
图9.25 正确设置了Fallback的使用透明度测试的物体

![alpha_test_shadow_2.png-75.7kB](http://static.zybuluo.com/candycat/g4hli2g5m1371d7h1bowc4jj/alpha_test_shadow_2.png)
图9.26 正确设置了Cast Shadow属性的使用透明度测试的物体

![alpha_blend_shadow0.png-88.6kB](http://static.zybuluo.com/candycat/4qjn2sb071h7akbwxx7n5nre/alpha_blend_shadow0.png)
图9.27 把使用了透明度混合的Unity Shader的Fallback设置为内置的Transparent/VertexLit。半透明物体不会向下方的平面投射阴影，也不会接收来自右侧平面的阴影，它看起来就像是完全透明一样

![alpha_blend_shadow1.png-94.9kB](http://static.zybuluo.com/candycat/00c0x6mhf74ru1kd9ejdwlko/alpha_blend_shadow1.png)
图9.28 把Fallback设为VertexLit来强制为半透明物体生成阴影





### 第10章 高级纹理





![cubemap_sample.png-20.1kB](http://static.zybuluo.com/candycat/2r8xxicnsapkqbteoto79pxu/cubemap_sample.png)
图10.1 对立方体纹理的采样

![skybox_mat.png-159kB](http://static.zybuluo.com/candycat/wg85b0wb37t0q76lbq3y6zxs/skybox_mat.png)
图10.2 天空盒子材质

![lighting_skybox.png-28.7kB](http://static.zybuluo.com/candycat/xyoodrunl4mbbgv5brqjyq0f/lighting_skybox.png)
图10.3 为场景使用自定义的天空盒子

![skybox_scene.png-346.5kB](http://static.zybuluo.com/candycat/s0ntkfe1bez8zovfz9c9m7d2/skybox_scene.png)
图10.4 使用了天空盒子的场景

![render_into_cubemap.png-123kB](http://static.zybuluo.com/candycat/l0sdnfmt2sqz1me0ffh2lv83/render_into_cubemap.png)
图10.5 使用脚本创建立方体纹理

![render_to_cubemap.png-133.8kB](http://static.zybuluo.com/candycat/0xj35c2xyghr94qejg8gu75n/render_to_cubemap.png)
图10.6 使用脚本渲染立方体纹理

![reflection.png-400.5kB](http://static.zybuluo.com/candycat/kvbrukc9u4z3gws4z4xyjzae/reflection.png)
图10.7 使用了反射效果的Teapot模型

![snell_law.png-28.6kB](http://static.zybuluo.com/candycat/mrqwqi3up3itfrnw2gbc0v81/snell_law.png)
图10.8 斯涅尔定律

![refraction.png-377.1kB](http://static.zybuluo.com/candycat/r895gindngpqsbtf3bt9s8iz/refraction.png)
图10.9 使用了折射效果的Teapot模型

![fresnel.png-64.6kB](http://static.zybuluo.com/candycat/1wv42r40xkxm2px9kwdgmsd2/fresnel.png)
图10.10 使用了菲涅耳反射的Teapot模型

![mirror.png-342.1kB](http://static.zybuluo.com/candycat/p6xmvccttgbwoontkcz2aw6s/mirror.png)
图10.11 镜子效果

![render_texture.png-113.3kB](http://static.zybuluo.com/candycat/wnvt1efwxapznql1x19hp07i/render_texture.png)
图10.12 左图：把摄像机的Target Texture设置成自定义的渲染纹理。右图：渲染纹理使用的纹理设置

![glass.png-462.9kB](http://static.zybuluo.com/candycat/fwsiw50bmkvtvvfchazzjc4g/glass.png)
图10.13 玻璃效果

![glass_cubemap.png-140.2kB](http://static.zybuluo.com/candycat/kk334ihfwvw6uf7d457kin3e/glass_cubemap.png)
图10.14 本例使用的立方体纹理

![procedural_texture.png-111.3kB](http://static.zybuluo.com/candycat/5kw303ah2c3bgda33qhg69o1/procedural_texture.png)
图10.15 脚本生成的程序纹理

![procedural_texture_multi.png-62.8kB](http://static.zybuluo.com/candycat/swke90qelg832pfi56wf5csa/procedural_texture_multi.png)
图10.16　调整程序纹理的参数来得到不同的程序纹理

![subtance_material.png-41.1kB](http://static.zybuluo.com/candycat/cvzw3s5ctqu6qcuglf73e867/subtance_material.png)
图10.17　后缀为.sbsar的Substance材质

![subtance_material_asset.png-78.8kB](http://static.zybuluo.com/candycat/nsmnfpzjoomtmjk9q2ggvl9x/subtance_material_asset.png)
图10.18　程序纹理资源

![subtance_material_multi.png-183.5kB](http://static.zybuluo.com/candycat/qqtq4kuo1cioe5hr7r9idcs5/subtance_material_multi.png)
图10.19　调整程序纹理属性可以得到看似完全不同的程序材质效果





### 第11章 让画面动起来





![boom.png-140.2kB](http://static.zybuluo.com/candycat/l0k525lbsoqgxvy6hx0qcypv/boom.png)
图11.1 本节使用的序列帧图像

![boom_sequence.png-37.6kB](http://static.zybuluo.com/candycat/i1erzd6uj2qtauhnhpyoghkw/boom_sequence.png)
图11.2 使用序列帧动画来实现爆炸效果

![scroll_background.png-228.5kB](http://static.zybuluo.com/candycat/2kti0v0qeqdg3nh4k1g1tvd9/scroll_background.png)
图11.3 无限滚动的背景（纹理来源：forest-background © 2012-2013 Julien Jorge julien.jorge@stuff-o-matic.com）

![river.png-242.7kB](http://static.zybuluo.com/candycat/zbckc0o5c8ygxj52o1vjl6gn/river.png)
图11.4 使用顶点动画来模拟2D的河流

![basis_vector.png-76.2kB](http://static.zybuluo.com/candycat/nmwj4c59j8dif8828fehq477/basis_vector.png)
图11.5 法线固定（总是指向视角方向）时，计算广告牌技术中的三个正交基的过程

![billboard.png-86.8kB](http://static.zybuluo.com/candycat/bndvgjiho7jr1zpercpxh6iu/billboard.png)
图11.6 广告牌效果。左图显示了摄像机和5个广告牌之间的位置关系，摄像机是从斜上方向下观察它们的。中间的图显示了当Vertical Restraints属性为1，即固定法线方向为观察视角时所得到的效果，可以看出，所有的广告牌都完全面朝摄像机。右图显示了当Vertical Restraints属性为0，即固定指向上的方向为(0, 1, 0)时所得到的效果，可以看出，广告牌虽然最大限度地面朝摄像机，但其指向上的方向并未发生改变

![wrong_shadow.png-147.3kB](http://static.zybuluo.com/candycat/29aprg3n5fsuxup63wk5ovzl/wrong_shadow.png)
图11.7 当进行顶点动画时，如果仍然使用内置的ShadowCaster Pass来渲染阴影，可能会得到错误的阴影效果

![right_shadow.png-43.8kB](http://static.zybuluo.com/candycat/bfvx4iycwdjnraykcnvjpw3g/right_shadow.png)
图11.8 使用自定义的ShadowCaster Pass 为变形物体绘制正确的阴影





### 第12章 屏幕后处理效果





![brtsatcon.png-651.1kB](http://static.zybuluo.com/candycat/szhonaye4dir2otxjsjc0836/brtsatcon.png)
图12.1 左图：原效果。右图：调整了亮度（值为1.2）、饱和度（值为1.6）和对比度（值为1.2）后的效果

![script_shader.png-16.6kB](http://static.zybuluo.com/candycat/gj5f0q2eqsnw6vb6qjslw2u5/script_shader.png)
图12.2 为脚本设置Shader的默认值

![edge_detection.png-717.9kB](http://static.zybuluo.com/candycat/88uix76d65ca3yu592w0okhh/edge_detection.png)
图12.3 左图：12.2节得到的结果。 右图：进行边缘检测后的效果

![convolution.png-15.1kB](http://static.zybuluo.com/candycat/dvch7lp9z5d9rp4o0c1edjep/convolution.png)
图12.4 卷积核与卷积。使用一个3×3大小的卷积核对一张5×5大小的图像进行卷积操作，当计算图中红色方块对应的像素的卷积结果时，我们首先把卷积核的中心放置在该像素位置，翻转核之后再依次计算核中每个元素和其覆盖的图像像素值的乘积并求和，得到新的像素值

![edge_detection_kernel.png-19.8kB](http://static.zybuluo.com/candycat/bm2nnarbl2h6fmmjq1gsfb7c/edge_detection_kernel.png)
图12.5 三种常见的边缘检测算子

![edge_only.png-266.5kB](http://static.zybuluo.com/candycat/qg856glqkbkaw28vmwl59kic/edge_only.png)
图12.6 只显示边缘的屏幕效果

![gaussian_blur.png-703.8kB](http://static.zybuluo.com/candycat/0y9xt8awtvueymd63g829vmu/gaussian_blur.png)
图12.7 左图：原效果。右图：高斯模糊后的效果

![gaussian_kernel.png-21.2kB](http://static.zybuluo.com/candycat/qdi1a1gaicihr3tju2acbcdc/gaussian_kernel.png)
图12.8 一个5×5大小的高斯核。左图显示了标准方差为1的高斯核的权重分布。我们可以把这个二维高斯核拆分成两个一维的高斯核（右图）

![800px-Elephants_Dream_-_Emo_and_Proog.jpg-41.9kB](http://static.zybuluo.com/candycat/0k9u1k5rrg9cq4gj4mwj1l0x/800px-Elephants_Dream_-_Emo_and_Proog.jpg)
图12.9 动画短片《大象之梦》中的Bloom效果。光线透过门扩散到了周围较暗的区域中

![bloom.png-772.3kB](http://static.zybuluo.com/candycat/gt2h3xoo89hmvm8o85pso5uh/bloom.png)
图12.10 左图：原效果。右图：Bloom处理后的效果

![motion_blur.png-770.9kB](http://static.zybuluo.com/candycat/ryde8k1k1bm5j7dxgdo5w0ks/motion_blur.png)
图12.11 左图：原效果。右图：应用运动模糊后的效果





### 第13章 使用深度和法线纹理





![projection_matrix.png-150.4kB](http://static.zybuluo.com/candycat/u6fma5c4boo56dgjbgczlb2i/projection_matrix.png)
图13.1 在透视投影中，投影矩阵首先对顶点进行了缩放。在经过齐次除法后，透视投影的裁剪空间会变换到一个立方体。图中标注了4个关键点经过投影矩阵变换后的结果

![orthographic_matrix.png-129.6kB](http://static.zybuluo.com/candycat/8idbd0mykpsqnj16t84uwsml/orthographic_matrix.png)
图13.2 在正交投影中，投影矩阵对顶点进行了缩放。在经过齐次除法后，正交投影的裁剪空间会变换到一个立方体。图中标注了4个关键点经过投影矩阵变换后的结果

![check_texture.png-161.3kB](http://static.zybuluo.com/candycat/xnqw3nkojdxml562evws8aug/check_texture.png)
图13.3 使用Frame Debugger查看深度纹理（左）和深度+法线纹理（右）。如果当前摄像机需要生成深度和法线纹理，帧调试器的面板中就会出现相应的渲染事件。只要单击对应的事件就可以查看得到的深度和法线纹理

![check_texture_code.png-84kB](http://static.zybuluo.com/candycat/kp57syi72i7jloyghgbeqy82/check_texture_code.png)
图13.4 左图：线性空间下的深度纹理。右图：解码后并且被映射到[0, 1]范围内的视角空间下的法线纹理

![fog.png-627.5kB](http://static.zybuluo.com/candycat/6yzf4h789v3117qpa4t2k931/fog.png)
图13.5 左图：原效果。右图：添加全局雾效后的效果

![frustum.png-33.5kB](http://static.zybuluo.com/candycat/cisfq83ut1mx2ou313e1nqg2/frustum.png)
图13.6 计算interpolatedRay

![world_dist.png-18.6kB](http://static.zybuluo.com/candycat/6h2nnw3gwzcio21jbji2o2dw/world_dist.png)
图13.7 采样得到的深度值并非是点到摄像机的欧式距离

![over_edge.png-819kB](http://static.zybuluo.com/candycat/20oe6ovk2wn4ko2el5ldwfs9/over_edge.png)
图13.8 左图：原效果。右图：直接对颜色图像进行边缘检测的结果

![edge_detect.png-452.9kB](http://static.zybuluo.com/candycat/snzxjfahsz29po5mcrfrczmu/edge_detect.png)
图13.9 在深度和法线纹理上进行更健壮的边缘检测。左图：在原图上描边的效果。右图：只显示描边的效果

![Roberts.png-15.7kB](http://static.zybuluo.com/candycat/ziah5yj1twj4nva7ldvw8dnk/Roberts.png)
图13.10 Roberts算子





### 第14章 非真实感渲染





![okami_announce_screens6.jpg-169.9kB](http://static.zybuluo.com/candycat/aa2hjqkoibcqmq5g5azdkrfb/okami_announce_screens6.jpg)
图14.1 游戏《大神》（英文名：Okami）的游戏截图

![toon_shading.png-74.1kB](http://static.zybuluo.com/candycat/0x7o2vyl6fn74gwtunvdgufp/toon_shading.png)
图14.2 卡通风格的渲染效果

![antialiasing.png-138.4kB](http://static.zybuluo.com/candycat/z8c9f6kzclslbl0wdw7gxach/antialiasing.png)
图14.3 左图：未对高光区域进行抗锯齿处理。右图：使用fwidth函数对高光区域进行抗锯齿处理

![TAM.png-127.6kB](http://static.zybuluo.com/candycat/9h63lflg1a7f759pw5cwfqvz/TAM.png)
图14.4 一个TAM的例子（来源：Praun E, et al. Real-time hatching[4](http://static.zybuluo.com/candycat/qwr4r6aglmod38w2k1e0dq7h/CopyDataToGPU.png)）

![hatching.png-268.1kB](http://static.zybuluo.com/candycat/60jzr7ly5yqqcg09rfrc3icb/hatching.png)
图14.5 素描风格的渲染效果





### 第15章 使用噪声





![burn.png-429.1kB](http://static.zybuluo.com/candycat/43pgznadojl5el7s23zpki7x/burn.png)
图15.1 箱子的消融效果

![burn_noise.png-84.8kB](http://static.zybuluo.com/candycat/l8caf290oitxfnenqu38ed95/burn_noise.png)
图15.2 消融效果使用的噪声纹理

![water.png-722.5kB](http://static.zybuluo.com/candycat/rgxn8cpsc4isivqouvbxtev7/water.png)
图15.3 包含菲涅耳反射的水面波动效果。在左图中，视角方向和水面法线的夹角越大，反射效果越强。在右图中，视角方向和水面法线的夹角越大，折射效果越强

![cubemap.png-128.3kB](http://static.zybuluo.com/candycat/lh1zewua7dl2p8olhmctowoz/cubemap.png)
图15.4 本例使用的立方体纹理

![water_noise.png-202kB](http://static.zybuluo.com/candycat/unuc9j0kp9fffr7jcnbowvzi/water_noise.png)
图15.5 水波效果使用的噪声纹理。左图：噪声纹理的灰度图。右图：由左图生成的法线纹理

![fog.png-493.9kB](http://static.zybuluo.com/candycat/dmrvnch1muikmc6f50sdwdho/fog.png)
图15.6 左图：均匀雾效。右图：使用噪声纹理后的非均匀雾效

![fog_noise.jpg-13kB](http://static.zybuluo.com/candycat/kfctu0s78fl2pepr9h1hgjpo/fog_noise.jpg)
图15.7 本节使用的噪声纹理





### 第16章 Unity中的渲染优化技术





![render_static_window.png-156.1kB](http://static.zybuluo.com/candycat/mw2e3pfqk097fps9wbcwv8ff/render_static_window.png)
图16.1 Unity 5的渲染统计窗口

![profiler.png-122.5kB](http://static.zybuluo.com/candycat/f1fpglqqgcg7q17tum55e8bh/profiler.png)
图16.2 使用Unity的性能分析器中的渲染区域来查看更多关于渲染的统计信息

![frame_debugger.png-84.3kB](http://static.zybuluo.com/candycat/3qa6mzh0mc1q7jiqhaf3j7mv/frame_debugger.png)
图16.3 使用帧调试器来查看单独的draw call的绘制结果

![dynamic_batching0.png-138.9kB](http://static.zybuluo.com/candycat/ytyrujgdcz4dxpvm8nw3tibd/dynamic_batching0.png)
图16.4 动态批处理

![dynamic_batching1.png-138.9kB](http://static.zybuluo.com/candycat/0l9c6cjb4czi02hxr8e2ij0o/dynamic_batching1.png)
图16.5 多光源对动态批处理的影响结果

![static_batching0.png-112.9kB](http://static.zybuluo.com/candycat/h7pzd9j05aelvv6cafs7juzv/static_batching0.png)
图16.6 静态批处理前的渲染统计数据

![mark_static.png-22.3kB](http://static.zybuluo.com/candycat/jkgbb245hcnoxzq4k3go3yba/mark_static.png)
图16.7 把物体标志为Static

![static_batching1.png-112.3kB](http://static.zybuluo.com/candycat/p7h3m5syxv9g7i928zohzhas/static_batching1.png)
图16.8 静态批处理

![combined_mesh.png-152.1kB](http://static.zybuluo.com/candycat/kfz63didqcnctti7ft8lvtpw/combined_mesh.png)
图16.9 静态批处理中Unity会合并所有被标识为“Static”的物体

![vbo.png-92kB](http://static.zybuluo.com/candycat/u9o9tk9oispyksk3ag41an3x/vbo.png)
图16.10 静态批处理会占用更多的内存。左图：静态批处理前的渲染统计数据。右图：静态批处理后的渲染统计数据

![static_batching2.png-113.6kB](http://static.zybuluo.com/candycat/zul250cb0n5x5w5821tu4xwd/static_batching2.png)
图16.11 处理其他逐像素光的Pass不会被静态批处理

![advance_texture.png-96.6kB](http://static.zybuluo.com/candycat/58dcw7v9r39i2p2izrtxq5bs/advance_texture.png)
图16.12 Unity的高级纹理设置面板





### 第17章 Surface Shader探秘





![bumped_diffuse.png-164.7kB](http://static.zybuluo.com/candycat/slo759tsffn90428bqqkt054/bumped_diffuse.png)
图17.1 表面着色器的例子。左图：在一个平行光下的效果。右图：添加了一个点光源（蓝色）和一个聚光灯（紫色）后的效果

![generated_code.png-28.9kB](http://static.zybuluo.com/candycat/rt3i7s74tdilo8185rexkowi/generated_code.png)
图17.2 查看表面着色器生成的代码

![pipeline.png-171.9kB](http://static.zybuluo.com/candycat/rokaz0qqzk11hyj7ntkss3ze/pipeline.png)
图17.3 表面着色器的渲染计算流水线。黄色：可以自定义的函数。灰色：Unity自动生成的计算步骤

![normal_extrusion.png-127.3kB](http://static.zybuluo.com/candycat/bhggsxnr7rlhkzs8u68mqarn/normal_extrusion.png)
图17.4 沿顶点法线对模型进行膨胀。左图：膨胀前。右图：膨胀后





### 第18章 基于物理的渲染





![reflect_refract.png-26.9kB](http://static.zybuluo.com/candycat/nw3v0p25h9165552cshmr1t1/reflect_refract.png)
图18.1 在理想的边界处，折射率的突变会把光线分成两个方向

![rought_smooth.png-64.6kB](http://static.zybuluo.com/candycat/zmrvmeo27ach7kjpxm1grnwb/rought_smooth.png)
图18.2 左图：光滑表面的微平面的法线变化较小，反射光线的方向变化也更小。 右图：粗糙表面的微平面的法线变化较大，反射光线的方向变化也更大

![subsurface_scattered_light.png-36.3kB](http://static.zybuluo.com/candycat/ezo6d9xa3vv6l97hdy48jltc/subsurface_scattered_light.png)
图18.3 微表面对光的折射。这些被折射的光中一部分被吸收，一部分又被散射到外部

![surface.png-42.5kB](http://static.zybuluo.com/candycat/th1ophcgurbsh1jbobzz2d6k/surface.png)
图18.4 次表面散射。左图：次表面散射的光线会从不同于入射点的位置射出。如果这些距离值小于需要被着色的像素大小，那么渲染就可以完全在局部完成（右图）。否则，就需要使用次表面散射渲染技术

![brdf.png-47.1kB](http://static.zybuluo.com/candycat/08orrgge69y3d3zgp4gfpcn9/brdf.png)
图18.5 BRDF描述的两种现象。高光反射部分用于描述反射，漫反射部分用于描述次表面散射

![m_h.png-90.5kB](http://static.zybuluo.com/candycat/d03qynt6prxeq7cep9b1jl91/m_h.png)
图18.6 （a）那些m=h的微面元会恰好把入射光从I反射到v上，只有这部分微面元才可以添加到BRDF的计算中。（b）一部分满足（a）的微面元会在I方向上被其他微面元遮挡住，它们不会接受到光照，因此会形成阴影。（c）还有一部分满足（a）的微面元会在反射方向v上被其他微面元挡住，因此，这部分反射光也不会被看到

![standard_shader.png-276.6kB](http://static.zybuluo.com/candycat/8yd8tgsx8x1tvdcwuxxowgt3/standard_shader.png)
图18.7 Standard Shader中前向渲染路径使用的Pass（简化版本的PBS使用了VertexOutputBaseSimple等结构体来代替相应的结构体）

![calibration_charts.png-387.8kB](http://static.zybuluo.com/candycat/kpx9eqzt6xjtw7lp9uac9qc8/calibration_charts.png)
图18.8 Unity提供的校准表格。左图：金属工作流 使用的校准表格。右图：高光反射工作流使用的校准表格

![metallic_workflow.png-181.6kB](http://static.zybuluo.com/candycat/0y8tojxhwa92hjy4oo20ii9p/metallic_workflow.png)
图18.9 使用金属工作流来实现不同类型的材质。左边的球体：金属材质。右边的球体：塑料材质

![pbs_scene.png-625.7kB](http://static.zybuluo.com/candycat/rre47eai63qgeh811clxbev2/pbs_scene.png)
图18.10 在Unity 5中使用基于物理的渲染技术，场景在不同光照下的渲染结果

![lighting_inspector.png-48.9kB](http://static.zybuluo.com/candycat/829ewyjmvzjm082xpyysvqfz/lighting_inspector.png)
图18.11 光照面板下的Scene标签页

![reflect_source.png-349.6kB](http://static.zybuluo.com/candycat/nlh6q7gqgwlbitske1z8938i/reflect_source.png)
图18.12 左图：当关闭场景中的所有光源并把环境光照强度设为0后，使用了Standard Shader的物体仍然具有光照效果。右图：在左图的基础上，把反射源设置为空，使得物体不接受任何默认的反射信息

![direction_light.png-29.3kB](http://static.zybuluo.com/candycat/x7cxbmmb2xdzke3m0asowtu9/direction_light.png)
图18.13 使用的平行光

![bounce_intensity.png-645.9kB](http://static.zybuluo.com/candycat/61ycjyc3k04bjh8sai6womkn/bounce_intensity.png)
图18.14 左图：将Bounce Intensity设置为0，物体不再受到间接光照的影响，木屋内阴影部分的可见细节很少。右图：将Bounce Intensity设为8，阴影部分的细节更加清楚

![reflection_probe.png-615.8kB](http://static.zybuluo.com/candycat/twic91rz1143c14rc0t1n1ie/reflection_probe.png)
图18.15 左图：未使用反射探针。右图：在场景中放置了两个反射探针，注意墙上的盾牌与左图的差别

![interreflection.png-338.2kB](http://static.zybuluo.com/candycat/d7amfp6yscz10g5yk0kybwd1/interreflection.png)
图18.16 使用反射探针实现相互反射的效果

![linear_space.png-611.4kB](http://static.zybuluo.com/candycat/umachb7kklgerrvsphv7yyoj/linear_space.png)
图18.17 左图：在线性空间下的渲染结果。右图：在伽马空间下的渲染结果

![gamma_chart.png-29.3kB](http://static.zybuluo.com/candycat/uizo2ug3l5ovy68zbn9afde0/gamma_chart.png)
图18.18 人眼更容易感知暗部区域的变换，而对较亮区域的变化比较不敏感

![encoding_display_gamma.png-37.5kB](http://static.zybuluo.com/candycat/2y5h6wx9hupw5nv2ugtseyqn/encoding_display_gamma.png)
图18.19 编码伽马和显示伽马

![gamma_light.png-32.1k《Unity Shader入门精要》随书彩色插图

------

说明：本页面是书籍《Unity Shader入门精要》的随书彩图集锦，包含了书中所有的插图，使用时可通过图片编号进行搜索。
作者：冯乐乐
邮箱：lelefeng1992@gmail.com

------

### 前言



![shadertoy.png-286.5kB](http://static.zybuluo.com/candycat/x27bgzdj1cmfbzxa43z8t5qw/shadertoy.png)



### 第2章 渲染流水线




![流水线.png-83.4kB](http://static.zybuluo.com/candycat/zqt40itigpzl8qkn30m433g6/%E6%B5%81%E6%B0%B4%E7%BA%BF.png)
图2.1　真实生活中的流水线

![概念流水线.png-16.9kB](http://static.zybuluo.com/candycat/c0opg7bab4cwzyok5vek52hs/%E6%A6%82%E5%BF%B5%E6%B5%81%E6%B0%B4%E7%BA%BF.png)
图2.2 渲染流水线中的三个概念阶段

![CopyDataToGPU.png-86.5kB](http://static.zybuluo.com/candycat/qwr4r6aglmod38w2k1e0dq7h/CopyDataToGPU.png)
图2.3 渲染所需的数据（两张纹理以及3个网格）从硬盘最终加载到显存中。在渲染时，GPU可以快速访问这些数据

![SetRenderState.png-157.1kB](http://static.zybuluo.com/candycat/gld5mfj5o10kardzyn10p5a6/SetRenderState.png)
图2.4 在同一状态下渲染三个网格。由于没有更改渲染状态，因此三个网格的外观看起来像是同一种材质的物体。

![DrawCall.png-59.1kB](http://static.zybuluo.com/candycat/5nuo5d8oh1c8sxexr3d7e935/DrawCall.png)
图2.5 CPU通过调用Draw Call来告诉GPU开始进行一个渲染过程。一个Draw Call会指向本次调用需要渲染的图元列表

![GPU流水线.png-82.2kB](http://static.zybuluo.com/candycat/jundxsf604yuoy2zr3r1qkzp/GPU%E6%B5%81%E6%B0%B4%E7%BA%BF.png)
图2.6 GPU的渲染流水线实现。颜色表示了不同阶段的可配置性或可编程性：绿色表示该流水线阶段是完全可编程控制的，黄色表示该流水线阶段可以配置但不是可编程的，蓝色表示该流水线阶段是由GPU固定实现的，开发者没有任何控制权。实线表示该shader必须由开发者编程实现，虚线表示该Shader是可选的

![VertexShaderProcess.png-43kB](http://static.zybuluo.com/candycat/07rjqb1pkfipxiizr1nsywuf/VertexShaderProcess.png)
图2.7 GPU在每个输入的网格顶点上都会调用顶点着色器。顶点着色器必须进行顶点的坐标变换，需要时还可以计算和输出顶点的颜色。例如，我们可能需要进行逐顶点的光照

![Vertex Shader.png-34.9kB](http://static.zybuluo.com/candycat/2zpu3oh7n6kpy4rosqtjugcy/Vertex%20Shader.png)
图2.8 顶点着色器会将模型顶点的位置变换到齐次裁剪坐标空间下，进行输出后再由硬件做透视除法得到NDC下的坐标

![Clipping.png-25.5kB](http://static.zybuluo.com/candycat/08cvo0uahel9ygds4xkwrczp/Clipping.png)
图2.9 只有在单位立方体的图元才需要被继续处理。因此，完全在单位立方体外部的图元（红色三角形）被舍弃，完全在单位立方体内部的图元（绿色三角形）将被保留。和单位立方体相交的图元（黄色三角形）会被裁剪，新的顶点会被生成，原来在外部的顶点会被舍弃

![ScreenMapping.png-22.6kB](http://static.zybuluo.com/candycat/7xtfj07anrw60g4y7cadkd8h/ScreenMapping.png)
图2.10 屏幕映射将x、y坐标从（-1, 1）范围转换到屏幕坐标系中

![Screen Mapping_OpenGL_DirectX.png-26.9kB](http://static.zybuluo.com/candycat/ul58wnwn76vj0gm20m3xsi9g/Screen%20Mapping_OpenGL_DirectX.png)
图2.11 OpenGL和DirectX的屏幕坐标系差异。对于一张512*512大小的图像，在OpenGL中其（0, 0）点在左下角，而在DirectX中其(0, 0)点在左上角

![TriangleSetupAndTraversal.png-80kB](http://static.zybuluo.com/candycat/1ltkl388mkbbzbfgzm28f6gy/TriangleSetupAndTraversal.png)
图2.12 三角形遍历的过程。根据几何阶段输出的顶点信息，最终得到该三角网格覆盖的像素位置。对应像素会生成一个片元，而片元中的状态是对三个顶点的信息进行插值得到的。例如，对图2.12中三个顶点的深度进行插值得到其重心位置对应的片元的深度值为-10.0

![FragmentShader.png-42.4kB](http://static.zybuluo.com/candycat/lowfuoi0r43oxfgxkp9darur/FragmentShader.png)
图2.13 根据上一步插值后的片元信息，片元着色器计算该片元的输出颜色

![Per-fragment Operations.png-23.1kB](http://static.zybuluo.com/candycat/epejev04t6vudwsyo2el8rp0/Per-fragment%20Operations.png)
图2.14 逐片元操作阶段所做的操作。只有通过了所有的测试后，新生成的片元才能和颜色缓冲区中已经存在的像素颜色进行混合，最后再写入颜色缓冲区中

![Stencil Test_Depth Test.png-93.5kB](http://static.zybuluo.com/candycat/28t2ora2kenj1uudwfgfig95/Stencil%20Test_Depth%20Test.png)
图2.15 模板测试和深度测试的简化流程图。

![Blending.png-67.6kB](http://static.zybuluo.com/candycat/k7q79qcgoqkw8myu1lpuy7he/Blending.png)
图2.16 混合操作的简化流程图

![why_early_depth_test.png-18.7kB](http://static.zybuluo.com/candycat/kqngym2i5cvgo5bnkpfjabpi/why_early_depth_test.png)
图2.17 图示场景中包含了两个对象：球和长方体，绘制顺序是先绘制球（在屏幕上显示为圆），再绘制长方体（在屏幕上显示为长方形）。如果深度测试在片元着色器之后执行，那么在渲染长方体时，虽然它的大部分区域都被遮挡在球的后面，即它所覆盖的绝大部分片元根本无法通过深度测试，但是我们仍然需要对这些片元执行片元着色器，造成了很大的性能浪费

![OpenGL和DirectX.png-56.1kB](http://static.zybuluo.com/candycat/4x54y4f2kjlhil8wq7oi1fpa/OpenGL%E5%92%8CDirectX.png)
图2.18 CPU、OpenGL/DirectX、显卡驱动和GPU之间的关系

![CommandBuffer.png-49.9kB](http://static.zybuluo.com/candycat/h9oh7t35lbjrgogxywarmu55/CommandBuffer.png)
图2.19 命令缓冲区。CPU通过图像编程接口向命令缓冲区中添加命令，而GPU从中读取命令并执行。黄色方框内的命令就是Draw Call，而红色方框内的命令用于改变渲染状态。我们使用红色方框来表示改变渲染状态的命令， 是因为这些命令往往更加耗时

![SmallCommand.png-107.7kB](http://static.zybuluo.com/candycat/pef7ujj1xdzmzwdwz3n261rz/SmallCommand.png)
图2.20 命令缓冲区中的虚线方框表示GPU已经完成的命令。此时，命令缓冲区中没有可以执行的命令了，GPU处于空闲状态，而CPU还没有准备好下一个渲染命令。

![Batching.png-70.3kB](http://static.zybuluo.com/candycat/d6cxj75dc7hnzwd2jlcqlj4j/Batching.png)
图2.21 利用批处理，CPU在RAM把多个网格合并成一个更大的网格，再发送给GPU，然后在一个Draw Call中渲染它们。但要注意的是，使用批处理合并的网格将会使用同一种渲染状态。也就是说，如果网格之间需要使用不同的渲染状态，那么就无法使用批处理技术







### 第3章 Unity Shader基础





![material_shader.png-125.8kB](http://static.zybuluo.com/candycat/hojqrwubqu22k9jo0ues60hd/material_shader.png)
图3.1 Unity Shader和材质。首先创建需要的Unity Shader和材质，然后把Unity Shader赋给材质，并在材质面板上调整属性（如使用的纹理、漫反射系数等）。最后，将材质赋给相应的模型来查看最终的渲染效果

![mesh_renderer.png-41kB](http://static.zybuluo.com/candycat/fupmmv6n7raqei37v4jj6su1/mesh_renderer.png)
图3.2 将材质直接拖曳到模型的Mesh Renderer组件中

![material_inspector.png-119.4kB](http://static.zybuluo.com/candycat/936v924ooiux4x9v9l6nw7w2/material_inspector.png)
图3.3 材质提供了一种可视化的方式来调整着色器中使用的参数

![shader_import_settings.png-38kB](http://static.zybuluo.com/candycat/dwq288k4s50acnc7sx2wz9fp/shader_import_settings.png)
图3.4 Unity Shader的导入设置面板

![shader_compile_code.png-35.9kB](http://static.zybuluo.com/candycat/wvudje920on69gto9p9jq6bo/shader_compile_code.png)
图3.5 Gompile and show code下拉列表

![shaderlab_abstract.png-63.4kB](http://static.zybuluo.com/candycat/mfyfmiwipc220l4v8iowww6k/shaderlab_abstract.png)
图3.6 Unity Shader为控制渲染过程提供了一层抽象。如果没有使用Unity Shader（左图），开发者需要和很多文件和设置打交道，才能让画面呈现出想要的效果；而在Unity Shader的帮助下（右图），开发者只需要使用ShaderLab来编写Unity Shader文件就可以完成所有的工作

![shader_name.png-55.5kB](http://static.zybuluo.com/candycat/7u7q53pfa4pbtapi9wz9b6f7/shader_name.png)
图3.7 在Unity Shader的名称定义中利用 斜杠来组织在材质面板中的位置

![shaderlab_properties.png-33.2kB](http://static.zybuluo.com/candycat/izzjwk3okp3r41uok617ry8t/shaderlab_properties.png)
图3.8 不同属性类型在材质 面板中的显示结果

![shader_compile_code.png-35.9kB](http://static.zybuluo.com/candycat/55s9cmdps9zqm738ls4ibuho/shader_compile_code.png)
图3.9 在Unity Shader的导入设置面板中可以通过Compile and show code按钮来查看Unity对CG片段编译后的代码。通过单击Compile and show code按钮右端的倒三角可以打开下拉菜单，在这个下拉菜单中可以选择编译的平台种类，如只为当前的显卡设备编译特定的汇编代码，或为所有的平台编译汇编代码，我们也可以自定义选择编译到哪些平台上





### 第4章 学习Shader所需的数学基础





![little_cow.png-293.5kB](http://static.zybuluo.com/candycat/tdhtbh0rhx1dw94fbegmfxg9/little_cow.png)
图4.1 我们的农场游戏。我们的主角妞妞是一头长得最壮、好奇心很强的奶牛

![cartersian_fly.png-28kB](http://static.zybuluo.com/candycat/u6pb6kylub8zxfwxotxs3cbm/cartersian_fly.png)
图4.2 传说，笛卡尔坐标系来源于笛卡尔对天花板上一只苍蝇的运动轨迹的观察。笛卡尔发现，可以使用苍蝇距不同墙面的距离来描述它的当前位置

![2d_cartesian.png-36.4kB](http://static.zybuluo.com/candycat/in4byrrfu29pr19hhfmzaqsw/2d_cartesian.png)
图4.3 一个二维笛卡尔坐标系

![2d_cartesian_opengl_directx.png-33.1kB](http://static.zybuluo.com/candycat/s4twn4lnbvlac7ci3mwwbe4d/2d_cartesian_opengl_directx.png)
图4.4 在屏幕映射时，OpenGL和DirectX使用了不同方向的二维笛卡尔坐标系

![cow_cartesian.png-211.8kB](http://static.zybuluo.com/candycat/9n615pcahnqo38xx5dm8vxpi/cow_cartesian.png)
图4.5 笛卡尔坐标系可以让妞妞精确表述自己的位置

![3d_cartesian.png-22.7kB](http://static.zybuluo.com/candycat/tp39jr06yzo8u4gdzp0z1qqs/3d_cartesian.png)
图4.6 一个三维笛卡尔坐标系

![left_hand.png-40.5kB](http://static.zybuluo.com/candycat/7vdjcritmzv94yosp538yq7w/left_hand.png)
图4.7 左手坐标系

![right_hand.png-40kB](http://static.zybuluo.com/candycat/5llpe09e7f8mtdu7h49s88r1/right_hand.png)
图4.8 右手坐标系

![left_right_hand_rule.png-75.3kB](http://static.zybuluo.com/candycat/w5i9lq84fphxch5x8tjtzqo2/left_right_hand_rule.png)
图4.9 用左手法则和右手法则来判断旋转正方向

![cow_left_right.png-254.3kB](http://static.zybuluo.com/candycat/i65z04v7mbcufxsjkx7n0n67/cow_left_right.png)
图4.10 为了移动到新的位置，妞妞需要首先向某个方向平移1个单位，再向另一个方向平移4个单位，最后再向一个方向旋转60°

![cow_left_right_hand.png-295.8kB](http://static.zybuluo.com/candycat/janos0r95h321yeoeufigdog/cow_left_right_hand.png)
图4.11 左图和右图分别表示了在左手坐标系和右手坐标系中描述妞妞这次运动的结果，得到的数学描述是不同的

![unity_cartesian.png-173.2kB](http://static.zybuluo.com/candycat/7xx63gosl0504rj16wdcnare/unity_cartesian.png)
图4.12 在模型空间和世界空间中，Unity使用的是左手坐标系。图中，球的坐标轴显示了它在模型空间中的3个坐标轴（红色为x轴，绿色是y轴，蓝色是z轴）

![unity_camera_cartesian.png-25.1kB](http://static.zybuluo.com/candycat/lrhkf34n8p5fz7mzyro7r72m/unity_camera_cartesian.png)
图4.13 在Unity中，观察空间使用的是右手坐标系，摄像机的前向是z轴的负方向， z轴越小，物体的深度越大，离摄像机越远

![exercise_3.png-130.8kB](http://static.zybuluo.com/candycat/t5slprvqvmndc1yve7x0lquo/exercise_3.png)
图4.14 摄像机的位置是（0, 1, -10），球体的位置是（0, 1, 0）

![vector.png-8.9kB](http://static.zybuluo.com/candycat/8e49l43g2xhp9wfs6r526226/vector.png)
图4.15 一个二维向量以及它的头和尾

![point_vector.png-16.1kB](http://static.zybuluo.com/candycat/jwojplbtid4z6xiuw7dso9t0/point_vector.png)
图4.16 点和矢量之间的关系

![vector_scalar.png-53.9kB](http://static.zybuluo.com/candycat/py5slc3wo9v78lpb25xcdas0/vector_scalar.png)
图4.17 二维矢量和一些标量的乘法和除法

![vector_add_sub.png-52.8kB](http://static.zybuluo.com/candycat/2y7rr3t5j8bct6ocnlvpydp6/vector_add_sub.png)
图4.18 二维矢量的加法和减法

![vector_displacement.png-22.5kB](http://static.zybuluo.com/candycat/051rzkws7n2ii9wep4b04t8f/vector_displacement.png)
图4.19 使用矢量减法来计算从点a到点b的位移

![vector_magnitude.png-8.2kB](http://static.zybuluo.com/candycat/lk35xmttonr0qliblc5v5lpu/vector_magnitude.png)
图4.20 矢量的模

![unit_vector.png-30.7kB](http://static.zybuluo.com/candycat/mqfl49yeebwbqtc23i755qux/unit_vector.png)
图4.21 二维空间的单位矢量都会落在单位圆上

![projection.png-17.7kB](http://static.zybuluo.com/candycat/rlo1hwsdb334yi9i9vimdtko/projection.png)
图4.22 矢量b在单位矢量a方向上的投影

![dot_sign.png-22.9kB](http://static.zybuluo.com/candycat/wet7zoq1bssb0u8gm63zfmx6/dot_sign.png)
图4.23 点积的符号

![dot_cos.png-14.1kB](http://static.zybuluo.com/candycat/xnouckzvbcb59nqcanijjpx7/dot_cos.png)
图4.24 两个单位矢量进行点积

![vector_cross_diagram.png-32.1kB](http://static.zybuluo.com/candycat/yrl5ol849v5h8892l4bqlgrh/vector_cross_diagram.png)
图4.25 三维矢量叉积的计算规律。不同颜色的线表示了计算结果矢量中对应颜色的分量的计算路径。以红色为例，即结果矢量的第一个分量，它是从第一个矢量的y分量出发乘以第二个矢量的z分量，再减去第一个矢量的z分量和第二矢量的y分量的乘积

![vector_cross_length.png-13kB](http://static.zybuluo.com/candycat/fh9vcn0q1g5te175pqg9beu3/vector_cross_length.png)
图4.26 使用矢量a和矢量b构建一个平行四边形

![vector_cross.png-27.2kB](http://static.zybuluo.com/candycat/0d3l6dqc7q6d3h6vxkqjqo99/vector_cross.png)
图4.27 分别使用左手坐标系和右手坐标系得到的叉积结果

![vector_cross_right_hand.png-46.6kB](http://static.zybuluo.com/candycat/t6i0a60k7rd05a5url0wljcl/vector_cross_right_hand.png)
图4.28 使用右手法则判断右手坐标系中a×b的方向

![exercise_cross.png-26.1kB](http://static.zybuluo.com/candycat/5oy7iqjnkyi69v1d2sayhxf0/exercise_cross.png)
图4.29 三角形的三个顶点位于xy平面上，人眼位于z轴负方向，向z轴正方向观察

![matrix_mul.png-25kB](http://static.zybuluo.com/candycat/u6urub3wacveq0qcr6112we5/matrix_mul.png)
图4.30 计算c23的过程

![niuniu.png-273.2kB](http://static.zybuluo.com/candycat/ncg6g1ragp0bfufbm2m3ir2m/niuniu.png)
图4.31 场景中的妞妞（左图）和屏幕上的妞妞（右图）。妞妞想知道，自己的鼻子是如何被画到屏幕上的

![object_space.png-84.5kB](http://static.zybuluo.com/candycat/o85jqc1fw9rt10f0n485y9vt/object_space.png)
图4.32 在我们的农场游戏中，每个奶牛都有自己的模型坐标系。在模型坐标系中妞妞鼻子的位置是(0, 2, 4, 1)

![unity_transform.png-151.9kB](http://static.zybuluo.com/candycat/drp1660u59nwnw8d2hvb0rrg/unity_transform.png)
图4.33 Unity的Transform组件可以调节模型的位置.如果Transform有父节点，如图中的“Mesh”，那么Position将是在其父节点（这里是“Cow”）的模型空间中的位置；如果没有父节点，Position就是在世界空间中的位置

![world_space.png-378.7kB](http://static.zybuluo.com/candycat/ozup3egxnxqp21otm4z6jzhx/world_space.png)
图4.34 农场游戏中的世界空间。世界空间的原点被放置在农场的中心。左下角显示了妞妞在世界空间中所做的变换。我们想要把妞妞的鼻子从模型空间变换到世界空间中

![camera_space.png-346.2kB](http://static.zybuluo.com/candycat/8q0v8m4wwkm2h9homadyeear/camera_space.png)
图4.35 农场游戏中摄像机的观察空间。观察空间的原点位于摄像机处。注意在观察空间中，摄像机的前向是z轴的负方向（图中只画出了z轴正方向），这是因为Unity在观察空间中使用了右手坐标系。左下角显示了摄像机在世界空间中所做的变换。我们想要把妞妞的鼻子从世界空间变换到观察空间中

![camera_projection.png-299.3kB](http://static.zybuluo.com/candycat/wqkekwazaaordawbq21nj7hz/camera_projection.png)
图4.36 透视投影（左图）和正交投影（右图）。左下角分别显示了当前摄像机的投影模式和相关属性

![camera_frustum.png-301.2kB](http://static.zybuluo.com/candycat/b6wiym3nlkwimvnvgjgohhbz/camera_frustum.png)
图4.37 视锥体和裁剪平面。左图显示了透视投影的视锥体，右图显示了正交投影的视锥体

![projection_frustum.png-67.3kB](http://static.zybuluo.com/candycat/j6w23tgb5a1acjq6mr73ietq/projection_frustum.png)
图4.38 透视摄像机的参数对透视投影视锥体的影响

![projection_matrix0.png-135.1kB](http://static.zybuluo.com/candycat/tddwy4107pnswnbxydxc2rsp/projection_matrix0.png)
图4.39 在透视投影中，投影矩阵对顶点进行了缩放。图3.38中标注了4个关键点经过投影矩阵变换后的结果。从这些结果可以看出x、y、z和w分量的范围发生的变化

![orthographic_frustum.png-33.5kB](http://static.zybuluo.com/candycat/0r3xdlarpzqf94nfb304qihx/orthographic_frustum.png)
图4.40 正交摄像机的参数对正交投影视锥体的影响

![orthographic_matrix0.png-129.6kB](http://static.zybuluo.com/candycat/2j2ea1iexjim88y8towjkjlz/orthographic_matrix0.png)
图4.41 在正交投影中，投影矩阵对顶点进行了缩放。图中标注了4个关键点经过投影矩阵变换后的结果。从这些结果可以看出x、y、z和w分量范围发生的变化

![cow_camera.png-180.1kB](http://static.zybuluo.com/candycat/si6bqxafh76xku3i0bxp91lq/cow_camera.png)
图4.42 农场游戏使用的摄像机参数和游戏画面的横纵比

![projection_matrix1.png-131kB](http://static.zybuluo.com/candycat/7ozeba0c8nex3o4zr9z9nt4v/projection_matrix1.png)
图4.43 经过齐次除法后，透视投影的裁剪空间会变换到一个立方体

![orthographic_matrix1.png-105.6kB](http://static.zybuluo.com/candycat/8921u8zbn1m38conxbed0nz5/orthographic_matrix1.png)
图4.44 经过齐次除法后，正交投影的裁剪空间会变换到一个立方体

![vertex_conversion.png-100.9kB](http://static.zybuluo.com/candycat/z0ibvp779phr1hb0l902n1qy/vertex_conversion.png)
图4.45 渲染流水线中顶点的空间变换过程

![space_handness.png-75.6kB](http://static.zybuluo.com/candycat/jxcomxjmrye6rczmlyw550wt/space_handness.png)
图4.46 Unity中各个坐标空间的旋向性

![normal_tangent.png-167.3kB](http://static.zybuluo.com/candycat/cjevn0tuacb13ssus1sj8ceo/normal_tangent.png)
图4.47 顶点的切线和法线。切线和法线互相垂直

![transform_normal.png-40.6kB](http://static.zybuluo.com/candycat/80ofuzudfjzrrl8r1gcxinse/transform_normal.png)
图4.48 进行非统一缩放时，如果使用和变换顶点相同的变换矩阵来变换法线，就会得到错误的结果，即变换后的法线方向与平面不再垂直

![screen_coord.png-9kB](http://static.zybuluo.com/candycat/9puxwch79e92gzv5xfrsh3qm/screen_coord.png)
图4.49 由片元的像素位置得到的图像

![difference_between_left_right.png-54.6kB](http://static.zybuluo.com/candycat/zvcl27rgm897ir8w18m1bii2/difference_between_left_right.png)
图4.50 图中两个坐标系的x轴和y轴是重合的，区别仅在于z轴的方向。左手坐标系的（0, 0, 1）点和右手坐标系中的（0, 0, 1）点是不同的，但它们旋转后的点却对应到了同一点

![difference_between_left_right_2.png-59.4kB](http://static.zybuluo.com/candycat/akhas8nqu68ps3rd1kuhi0hf/difference_between_left_right_2.png)
图4.51 绝对空间中的同一点，在左手和右手坐标系中进行同样角度的旋转，其旋转方向是不一样的。在左手坐标系中将按顺时针方向旋转，在右手坐标系中将按逆时针方向旋转

![exercise_cross2.png-34.4kB](http://static.zybuluo.com/candycat/tw8il4lajuaf6dxx7l0yj9zd/exercise_cross2.png)
图4.52 在左手坐标系中，如果叉积结果为负，那么3点的顺序是顺时针方向





### 第5章 开始Unity Shader学习之旅





![new_scene.png-74.3kB](http://static.zybuluo.com/candycat/9b4lok82evuyq772bhbnnl6x/new_scene.png)
图5.1 在Unity 5中新建一个场景得到的效果

![simple_shader.png-25.4kB](http://static.zybuluo.com/candycat/4se9aphevcooho5wm1bsqxm0/simple_shader.png)
图5.2 用一个最简单的顶点/片元着色器得到一个白色的球

![cginclude.png-27kB](http://static.zybuluo.com/candycat/umffe4syp5ttjtilp9ydyd2k/cginclude.png)
图5.3 Unity的内置着色器

![false_color.png-192.9kB](http://static.zybuluo.com/candycat/yao0f655aycbk2kehmleei2p/false_color.png)
图5.4 用假彩色对Unity Shader进行调试

![color_picker.png-53.8kB](http://static.zybuluo.com/candycat/tx3a01nq92yshsc1y72n6s4j/color_picker.png)
图5.5 使用颜色拾取器来查看调试信息

![frame_debugger.png-218.7kB](http://static.zybuluo.com/candycat/dx8svpr4bxtegcns8e50lgf6/frame_debugger.png)
图5.6 帧调试器

![frame_debugger_0.png-164.5kB](http://static.zybuluo.com/candycat/11gb131ywty31xni4smc77ol/frame_debugger_0.png)
图5.7 单击Knot的深度图渲染事件，在Game视图会显示该事件的效果，在Hierarchy视图中会高亮显示Knot对象，在帧调试器的右侧窗口会显示出该事件的细节

![2d_cartesian_opengl_directx.png-33.1kB](http://static.zybuluo.com/candycat/ninmtxykcrk7oywzvxirhn04/2d_cartesian_opengl_directx.png)
图5.8 OpenGL和DirectX使用了不同的屏幕空间坐标





### 第6章 Unity中的基础光照





![irradiance.png-60.3kB](http://static.zybuluo.com/candycat/tzgu5oq816ojbkjo4y05rvij/irradiance.png)
图6.1 在左图中，光是垂直照射到物体表面，因此光线之间的垂直距离保持不变；而在右图中，光是斜着照射到物体表面，在物体表面光线之间的距离是d/cosθ，因此单位面积上接收到的光线数目要少于左图

![scattering.png-37.1kB](http://static.zybuluo.com/candycat/7gu6p5xdmzngz53iaa011joy/scattering.png)
图6.2 散射时，光线会发生折射和反射现象。对于不透明物体，折射的光线会在物体内部继续传播，最终有一部分光线会重新从物体表面被发射出去

![specular.png-31.2kB](http://static.zybuluo.com/candycat/51iph9ayl3l22w3xuzeumwxf/specular.png)
图6.3 使用Phong模型计算高光反射

![Blinn.png-32.1kB](http://static.zybuluo.com/candycat/nntler7jilkso6zufrbw447c/Blinn.png)
图6.4 Blinn模型

![ambient.png-35.3kB](http://static.zybuluo.com/candycat/4pgo8idyb8gsjlq5xbynoj8d/ambient.png)
图6.5 在Unity的Window -> Lighting面板中，我们可以通过Ambient Source/Ambient Color/Ambient Intensity来控制场景中的环境光的颜色和强度

![diffuse_vertex_level.png-40.4kB](http://static.zybuluo.com/candycat/tow3hbf8of391rb7sumri3sy/diffuse_vertex_level.png)
图6.6 逐顶点的漫反射光照效果

![diffuse_pixel_level.png-40.1kB](http://static.zybuluo.com/candycat/6vlfiln2hnmhndp3m5uma9bs/diffuse_pixel_level.png)
图6.7 逐像素的漫反射光照效果

![diffuse_compare_all.png-86.9kB](http://static.zybuluo.com/candycat/kc9sg9dsvf7i23my26yii8gt/diffuse_compare_all.png)
图6.8 逐顶点漫反射光照、逐像素漫反射光照、半兰伯特光照的对比效果

![reflect.png-9.2kB](http://static.zybuluo.com/candycat/zldeemd0807hp485mkgp6qkr/reflect.png)
图6.9 CG的reflect函数

![specular_vertex_level.png-41.5kB](http://static.zybuluo.com/candycat/zw9y4jmxj7pivjakhb2tjcnm/specular_vertex_level.png)
图6.10 逐顶点的高光反射光照效果

![specular_pixel_level.png-40.8kB](http://static.zybuluo.com/candycat/ze75kza2bpckowcdfcuqsqx6/specular_pixel_level.png)
图6.11 逐像素的高光反射光照效果

![specular_compare_all.png-82.5kB](http://static.zybuluo.com/candycat/5d2r1xz062iykspwapu0txq1/specular_compare_all.png)
图6.12 逐顶点的高光反射光照、逐像素的高光反射光照（Phong光照模型）和Blinn-Phong高光反射光照的对比结果





### 第7章 基础纹理





![texture_coordinate.png-349.3kB](http://static.zybuluo.com/candycat/rcl2u5im3ef0pb1esf4pvz06/texture_coordinate.png)
图7.1 Unity中的纹理坐标

![single_texture.png-71.3kB](http://static.zybuluo.com/candycat/90xmbvepdh5lywclqutr989j/single_texture.png)
图7.2 使用单张纹理

![texture_tiling_offset.png-16.9kB](http://static.zybuluo.com/candycat/p60yfqpxafslgw0b8m3t2vd6/texture_tiling_offset.png)
图7.3 调节纹理的平铺（缩放）和偏移（平移）属性

![texture_properties.png-29kB](http://static.zybuluo.com/candycat/nfnonexamcr821gvsqfwm0rc/texture_properties.png)
图7.4 纹理的属性

![wrap_mode.png-68.9kB](http://static.zybuluo.com/candycat/fs3ikv46cf3h1rumombx5toy/wrap_mode.png)
图7.5 Wrap Mode决定了当纹理坐标超过[0, 1]范围后将会如何被平铺

![texture_offset.png-68.4kB](http://static.zybuluo.com/candycat/3pu5fg044fhfd9zcvhmx1mue/texture_offset.png)
图7.6 偏移（Offset）属性决定了纹理坐标的偏移量

![magnification.png-256.2kB](http://static.zybuluo.com/candycat/e15n8gjm48ldr8eoavr7p7k1/magnification.png)
图7.7 在放大纹理时，分别使用三种Filter Mode得到的结果

![mipmap.png-35.9kB](http://static.zybuluo.com/candycat/jtlnp9o3hnkv4sapauejzudg/mipmap.png)
图7.8 在Advanced模式下可以设置多级渐远纹理的相关属性

![minification.png-271.9kB](http://static.zybuluo.com/candycat/jphpd33ux984u48qtrebzb93/minification.png)
图7.9 从上到下： Point滤波 + 多级渐远纹理技术，Bilinear滤波 + 多级渐远纹理技术，Trilinear滤波 + 多级渐远纹理技术

![texture_quality.png-31.7kB](http://static.zybuluo.com/candycat/3tqq3cu9wdo0z874ukzje19h/texture_quality.png)
图7.10 选择纹理的最大尺寸和纹理模式

![heightmap.png-134.5kB](http://static.zybuluo.com/candycat/679mbns3qqorjgdlzjd9f64w/heightmap.png)
图7.11 高度图

![tangent_space.png-165.3kB](http://static.zybuluo.com/candycat/fpgdxhkx2vrfag4wpxkubh08/tangent_space.png)
图7.12 模型顶点的切线空间。其中，原点对应了顶点坐标，x轴是切线方向（t），y轴是副切线方向（b），z轴是法线方向（n）

![object_tangent_space_normal.png-320.3kB](http://static.zybuluo.com/candycat/cn4bj1pud3ttm5mrlfa4l891/object_tangent_space_normal.png)
图7.13 左图：模型空间下的法线纹理。右图：切线空间下的法线纹理

![normal_map.png-92.2kB](http://static.zybuluo.com/candycat/xwv6ca3g9fdhlnu1a48lw1o4/normal_map.png)
图7.14 使用法线纹理

![bump_scale.png-140.5kB](http://static.zybuluo.com/candycat/ewkjgj08b94xafdzgroq7wgh/bump_scale.png)
图7.15 使用Bump Scale属性来调整模型的凹凸程度

![texture_type_normal.png-29.8kB](http://static.zybuluo.com/candycat/98ol95g0rx90mbdan3fiw4n7/texture_type_normal.png)
图7.16 当使用UnpackNormal函数计算法线纹理中的法线方向时，需要把纹理类型标识为Normal map

![texture_type_heightmap.png-293.4kB](http://static.zybuluo.com/candycat/nd93fm3dgv4obtkxjo6dg2sg/texture_type_heightmap.png)
图7.17 当勾选了Create from Grayscale后，Unity会根据高度图来生成一张切线空间下的法线纹理

![ramp_texture.png-119.2kB](http://static.zybuluo.com/candycat/lqani27ay2sk4r52hgvz7fx1/ramp_texture.png)
图7.18 使用不同的渐变纹理控制漫反射光照，左下角给出了每张图使用的渐变纹理

![ramp_texture_wrap_mode.png-114.2kB](http://static.zybuluo.com/candycat/0wnw5wpwv2stmazzurh32jpt/ramp_texture_wrap_mode.png)
图7.19 Wrap Mode分别为Repeat和Clamp模式的效果对比

![mask_specular.png-142.4kB](http://static.zybuluo.com/candycat/h82ljkimcijox5hwj7ftpymy/mask_specular.png)
图7.20 使用高光遮罩纹理。从左到右：只包含漫反射，未使用遮罩的高光反射，使用遮罩的高光反射

![mask.png-671.4kB](http://static.zybuluo.com/candycat/bu4eyurnenwal307dwbhzp2r/mask.png)
图7.21 本节使用的高光遮罩纹理





### 第8章 透明效果





![render_order_0.png-10.7kB](http://static.zybuluo.com/candycat/48l0aapqc57v0gn367tk2akx/render_order_0.png)
图8.1 场景中有两个物体，其中A（黄色）是半透明物体，B（紫色）是不透明物体

![render_order_1.png-10.5kB](http://static.zybuluo.com/candycat/5k524ddo8qib31j6s4mhkekh/render_order_1.png)
图8.2 场景中有两个物体，其中A和B都是半透明物体

![render_order_3.png-15.3kB](http://static.zybuluo.com/candycat/sl85989h54upaju75zstyv0y/render_order_3.png)
图8.3 循环重叠的半透明物体总是无法得到正确的半透明效果

![render_order_2.png-30.4kB](http://static.zybuluo.com/candycat/hi3bbsss5t48uvmi83uzjle8/render_order_2.png)
图8.4 使用哪个深度对物体进行排序。红色点分别标明了网格上距离摄像机最近的点、最远的点以及网格中点

![transparent_texture.png-71.9kB](http://static.zybuluo.com/candycat/fq123k86x5alcbccjmv7gogl/transparent_texture.png)
图8.5 一张透明纹理，其中每个方格的透明度都不同

![alpha_test.png-55.9kB](http://static.zybuluo.com/candycat/w3n0yyn3rfwc0wv4dw7i02d2/alpha_test.png)
图8.6 透明度测试

![alpha_test_0.png-166.4kB](http://static.zybuluo.com/candycat/a4hmfr1eltd6shzthle7ed5q/alpha_test_0.png)
图8.7 随着Alpha cutoff参数的增大，更多的像素由于不满足透明度测试条件而被剔除

![alpha_blend.png-55.1kB](http://static.zybuluo.com/candycat/0voinls84at3n3mg77a13tdu/alpha_blend.png)
图8.8 透明度混合

![alpha_blend_0.png-138.7kB](http://static.zybuluo.com/candycat/5a1af3bgca3z399huyud2kwr/alpha_blend_0.png)
图8.9 随着Alpha Scale参数的增大，模型变得越来越透明

![transparent_order_wrong.png-94.7kB](http://static.zybuluo.com/candycat/4thev7v5xczq02bz824witrf/transparent_order_wrong.png)
图8.10 当模型网格之间有互相交叉的结构时，往往会得到错误的半透明效果

![alpha_blend_zwrite.png-87.9kB](http://static.zybuluo.com/candycat/1vknx9ilky82q0kmqnxns8aj/alpha_blend_zwrite.png)
图8.11 开启了深度写入的半透明效果

![blend.png-74.1kB](http://static.zybuluo.com/candycat/uvoq8qpet472e7fquzdu479t/blend.png)
图8.12 不同混合状态设置得到的效果

![alpha_test_both_sided.png-60.7kB](http://static.zybuluo.com/candycat/zcu57h732mubbea9ib45wx9u/alpha_test_both_sided.png)
图8.13 双面渲染的透明度测试的物体

![alpha_blend_both_sided.png-66.2kB](http://static.zybuluo.com/candycat/4tq24631e9aug7xswikf9awc/alpha_blend_both_sided.png)
图8.14 双面渲染的透明度混合的物体





### 第9章 更复杂的光照





![rendering_path_setting.png-30kB](http://static.zybuluo.com/candycat/n67qqzd3bc0q3gca2heih70h/rendering_path_setting.png)
图9.1 设置Unity项目的渲染路径

![rendering_path_camera.png-37.8kB](http://static.zybuluo.com/candycat/7wi9c0vibxtig4s1r45bugri/rendering_path_camera.png)
图9.2 摄像机组件的Rendering Path中的设置可以覆盖Project Settings中的设置

![light_type_mode.png-30.6kB](http://static.zybuluo.com/candycat/skolpwg0h7zzcey4gtl1rvc9/light_type_mode.png)
图9.3 设置光源的类型和渲染模式

![forward_rendering.png-175.5kB](http://static.zybuluo.com/candycat/575lq2zgnsaop3nw2miyobt3/forward_rendering.png)
图9.4 前向渲染的两种Pass

![directional_ligth.png-51.6kB](http://static.zybuluo.com/candycat/uadla1q69533nc71z7g7ep0g/directional_ligth.png)
图9.5 平行光

![point_ligtht.png-89.4kB](http://static.zybuluo.com/candycat/tvbpd08wgc0s1o31v4nw20ad/point_ligtht.png)
图9.6 点光源

![enable_light.png-63.6kB](http://static.zybuluo.com/candycat/8cpddt5rwnxg6ox6bml57ld7/enable_light.png)
图9.7 开启Scene视图中的光照

![spot_light.png-74.5kB](http://static.zybuluo.com/candycat/tx45g2n04xypq5cdlyblecrv/spot_light.png)
图9.8 聚光灯

![two_lights.png-79.4kB](http://static.zybuluo.com/candycat/bz1q9kyglm17psychsn255aq/two_lights.png)
图9.9 使用一个平行光和一个点光源共同照亮物体。右图显示了胶囊体、平行光和点光源在场景中的相对位置

![multi_lights.png-56.6kB](http://static.zybuluo.com/candycat/z4lor2cgc0gh8rwfjimk0ckq/multi_lights.png)
图9.10 使用1个平行光 + 4个点光源照亮一个物体

![frame_debugger.png-103.3kB](http://static.zybuluo.com/candycat/78c7qwpppd0h5baure1l9t1q/frame_debugger.png)
图9.11 打开帧调试器查看场景的绘制事件

![multi_lights_0.png-218.4kB](http://static.zybuluo.com/candycat/e4ruexwdln51zl9nrj8s6yrl/multi_lights_0.png)
图9.12 本例中的6个渲染事件，绘制顺序是从左到右、从上到下进行的

![multi_lights_1.png-100.8kB](http://static.zybuluo.com/candycat/d1wgzjrprligehvkdmq23pra/multi_lights_1.png)
图9.13 如果物体不在一个光源的光照范围内（从右图可以看出，胶囊体不在最左方的点光源的照明范围内），Unity是不会调用Additional Pass来为该物体处理该光源的

![light_not_important.png-70.8kB](http://static.zybuluo.com/candycat/joseae4o6388culiwx8tfntf/light_not_important.png)
图9.14 当把光源的Render Mode设为Not Important时，这些光源就不会按逐像素光来处理

![light_shadow.png-32.8kB](http://static.zybuluo.com/candycat/11n30be5vio56i8a35qdqzrd/light_shadow.png)
图9.15 开启光源的阴影效果

![mesh_renderer.png-20.3kB](http://static.zybuluo.com/candycat/tp559yfnp82fb3i5g5y5qc77/mesh_renderer.png)
图9.16 Mesh Renderer组件的Cast Shadows和Receive Shadows属性可以控制该物体是否投射/接收阴影

![shadow_0.png-34.4kB](http://static.zybuluo.com/candycat/rd60ljcaza6xcthui0q98m29/shadow_0.png)
图9.17 开启Cast Shadows和Receive Shadows，从而让正方体可以投射和接收阴影

![shadow_1.png-89kB](http://static.zybuluo.com/candycat/3t7vthpva2llk7madax2rcqs/shadow_1.png)
图9.18 把Cast Shadows设置为Two Sided可以让右侧平面的背光面也产生阴影

![shadow_2.png-40.5kB](http://static.zybuluo.com/candycat/d33yusj8nxye922idu6ws2xe/shadow_2.png)
图9.19 正方体可以接收来自右侧平面的阴影

![shadow_frame_debugger.png-81.6kB](http://static.zybuluo.com/candycat/3sjunj4mk8gizha7fve184m4/shadow_frame_debugger.png)
图9.20 使用帧调试器查看阴影绘制过程

![shadow_frame_debugger_0.png-83.1kB](http://static.zybuluo.com/candycat/c3c1kldvrbicscs1opg7ihjn/shadow_frame_debugger_0.png)
图9.21 正方体对深度纹理的更新结果

![shadow_frame_debugger_1.png-88.6kB](http://static.zybuluo.com/candycat/88mxjbzlwzyxsbncd8337dd1/shadow_frame_debugger_1.png)
图9.22 屏幕空间的阴影图

![shadow_frame_debugger_2.png-175.1kB](http://static.zybuluo.com/candycat/fv1abzu7knq289amxegwxqki/shadow_frame_debugger_2.png)
图9.23 Unity绘制屏幕阴影的过程

![alpha_test_shadow_0.png-62.8kB](http://static.zybuluo.com/candycat/v0wel6w64l5x0intcrfp3vdt/alpha_test_shadow_0.png)
图9.24 可以投射阴影的使用透明度测试的物体

![alpha_test_shadow_1.png-66.2kB](http://static.zybuluo.com/candycat/ap18z7090krmbw2ftx2u3e6z/alpha_test_shadow_1.png)
图9.25 正确设置了Fallback的使用透明度测试的物体

![alpha_test_shadow_2.png-75.7kB](http://static.zybuluo.com/candycat/g4hli2g5m1371d7h1bowc4jj/alpha_test_shadow_2.png)
图9.26 正确设置了Cast Shadow属性的使用透明度测试的物体

![alpha_blend_shadow0.png-88.6kB](http://static.zybuluo.com/candycat/4qjn2sb071h7akbwxx7n5nre/alpha_blend_shadow0.png)
图9.27 把使用了透明度混合的Unity Shader的Fallback设置为内置的Transparent/VertexLit。半透明物体不会向下方的平面投射阴影，也不会接收来自右侧平面的阴影，它看起来就像是完全透明一样

![alpha_blend_shadow1.png-94.9kB](http://static.zybuluo.com/candycat/00c0x6mhf74ru1kd9ejdwlko/alpha_blend_shadow1.png)
图9.28 把Fallback设为VertexLit来强制为半透明物体生成阴影





### 第10章 高级纹理





![cubemap_sample.png-20.1kB](http://static.zybuluo.com/candycat/2r8xxicnsapkqbteoto79pxu/cubemap_sample.png)
图10.1 对立方体纹理的采样

![skybox_mat.png-159kB](http://static.zybuluo.com/candycat/wg85b0wb37t0q76lbq3y6zxs/skybox_mat.png)
图10.2 天空盒子材质

![lighting_skybox.png-28.7kB](http://static.zybuluo.com/candycat/xyoodrunl4mbbgv5brqjyq0f/lighting_skybox.png)
图10.3 为场景使用自定义的天空盒子

![skybox_scene.png-346.5kB](http://static.zybuluo.com/candycat/s0ntkfe1bez8zovfz9c9m7d2/skybox_scene.png)
图10.4 使用了天空盒子的场景

![render_into_cubemap.png-123kB](http://static.zybuluo.com/candycat/l0sdnfmt2sqz1me0ffh2lv83/render_into_cubemap.png)
图10.5 使用脚本创建立方体纹理

![render_to_cubemap.png-133.8kB](http://static.zybuluo.com/candycat/0xj35c2xyghr94qejg8gu75n/render_to_cubemap.png)
图10.6 使用脚本渲染立方体纹理

![reflection.png-400.5kB](http://static.zybuluo.com/candycat/kvbrukc9u4z3gws4z4xyjzae/reflection.png)
图10.7 使用了反射效果的Teapot模型

![snell_law.png-28.6kB](http://static.zybuluo.com/candycat/mrqwqi3up3itfrnw2gbc0v81/snell_law.png)
图10.8 斯涅尔定律

![refraction.png-377.1kB](http://static.zybuluo.com/candycat/r895gindngpqsbtf3bt9s8iz/refraction.png)
图10.9 使用了折射效果的Teapot模型

![fresnel.png-64.6kB](http://static.zybuluo.com/candycat/1wv42r40xkxm2px9kwdgmsd2/fresnel.png)
图10.10 使用了菲涅耳反射的Teapot模型

![mirror.png-342.1kB](http://static.zybuluo.com/candycat/p6xmvccttgbwoontkcz2aw6s/mirror.png)
图10.11 镜子效果

![render_texture.png-113.3kB](http://static.zybuluo.com/candycat/wnvt1efwxapznql1x19hp07i/render_texture.png)
图10.12 左图：把摄像机的Target Texture设置成自定义的渲染纹理。右图：渲染纹理使用的纹理设置

![glass.png-462.9kB](http://static.zybuluo.com/candycat/fwsiw50bmkvtvvfchazzjc4g/glass.png)
图10.13 玻璃效果

![glass_cubemap.png-140.2kB](http://static.zybuluo.com/candycat/kk334ihfwvw6uf7d457kin3e/glass_cubemap.png)
图10.14 本例使用的立方体纹理

![procedural_texture.png-111.3kB](http://static.zybuluo.com/candycat/5kw303ah2c3bgda33qhg69o1/procedural_texture.png)
图10.15 脚本生成的程序纹理

![procedural_texture_multi.png-62.8kB](http://static.zybuluo.com/candycat/swke90qelg832pfi56wf5csa/procedural_texture_multi.png)
图10.16　调整程序纹理的参数来得到不同的程序纹理

![subtance_material.png-41.1kB](http://static.zybuluo.com/candycat/cvzw3s5ctqu6qcuglf73e867/subtance_material.png)
图10.17　后缀为.sbsar的Substance材质

![subtance_material_asset.png-78.8kB](http://static.zybuluo.com/candycat/nsmnfpzjoomtmjk9q2ggvl9x/subtance_material_asset.png)
图10.18　程序纹理资源

![subtance_material_multi.png-183.5kB](http://static.zybuluo.com/candycat/qqtq4kuo1cioe5hr7r9idcs5/subtance_material_multi.png)
图10.19　调整程序纹理属性可以得到看似完全不同的程序材质效果





### 第11章 让画面动起来





![boom.png-140.2kB](http://static.zybuluo.com/candycat/l0k525lbsoqgxvy6hx0qcypv/boom.png)
图11.1 本节使用的序列帧图像

![boom_sequence.png-37.6kB](http://static.zybuluo.com/candycat/i1erzd6uj2qtauhnhpyoghkw/boom_sequence.png)
图11.2 使用序列帧动画来实现爆炸效果

![scroll_background.png-228.5kB](http://static.zybuluo.com/candycat/2kti0v0qeqdg3nh4k1g1tvd9/scroll_background.png)
图11.3 无限滚动的背景（纹理来源：forest-background © 2012-2013 Julien Jorge julien.jorge@stuff-o-matic.com）

![river.png-242.7kB](http://static.zybuluo.com/candycat/zbckc0o5c8ygxj52o1vjl6gn/river.png)
图11.4 使用顶点动画来模拟2D的河流

![basis_vector.png-76.2kB](http://static.zybuluo.com/candycat/nmwj4c59j8dif8828fehq477/basis_vector.png)
图11.5 法线固定（总是指向视角方向）时，计算广告牌技术中的三个正交基的过程

![billboard.png-86.8kB](http://static.zybuluo.com/candycat/bndvgjiho7jr1zpercpxh6iu/billboard.png)
图11.6 广告牌效果。左图显示了摄像机和5个广告牌之间的位置关系，摄像机是从斜上方向下观察它们的。中间的图显示了当Vertical Restraints属性为1，即固定法线方向为观察视角时所得到的效果，可以看出，所有的广告牌都完全面朝摄像机。右图显示了当Vertical Restraints属性为0，即固定指向上的方向为(0, 1, 0)时所得到的效果，可以看出，广告牌虽然最大限度地面朝摄像机，但其指向上的方向并未发生改变

![wrong_shadow.png-147.3kB](http://static.zybuluo.com/candycat/29aprg3n5fsuxup63wk5ovzl/wrong_shadow.png)
图11.7 当进行顶点动画时，如果仍然使用内置的ShadowCaster Pass来渲染阴影，可能会得到错误的阴影效果

![right_shadow.png-43.8kB](http://static.zybuluo.com/candycat/bfvx4iycwdjnraykcnvjpw3g/right_shadow.png)
图11.8 使用自定义的ShadowCaster Pass 为变形物体绘制正确的阴影





### 第12章 屏幕后处理效果





![brtsatcon.png-651.1kB](http://static.zybuluo.com/candycat/szhonaye4dir2otxjsjc0836/brtsatcon.png)
图12.1 左图：原效果。右图：调整了亮度（值为1.2）、饱和度（值为1.6）和对比度（值为1.2）后的效果

![script_shader.png-16.6kB](http://static.zybuluo.com/candycat/gj5f0q2eqsnw6vb6qjslw2u5/script_shader.png)
图12.2 为脚本设置Shader的默认值

![edge_detection.png-717.9kB](http://static.zybuluo.com/candycat/88uix76d65ca3yu592w0okhh/edge_detection.png)
图12.3 左图：12.2节得到的结果。 右图：进行边缘检测后的效果

![convolution.png-15.1kB](http://static.zybuluo.com/candycat/dvch7lp9z5d9rp4o0c1edjep/convolution.png)
图12.4 卷积核与卷积。使用一个3×3大小的卷积核对一张5×5大小的图像进行卷积操作，当计算图中红色方块对应的像素的卷积结果时，我们首先把卷积核的中心放置在该像素位置，翻转核之后再依次计算核中每个元素和其覆盖的图像像素值的乘积并求和，得到新的像素值

![edge_detection_kernel.png-19.8kB](http://static.zybuluo.com/candycat/bm2nnarbl2h6fmmjq1gsfb7c/edge_detection_kernel.png)
图12.5 三种常见的边缘检测算子

![edge_only.png-266.5kB](http://static.zybuluo.com/candycat/qg856glqkbkaw28vmwl59kic/edge_only.png)
图12.6 只显示边缘的屏幕效果

![gaussian_blur.png-703.8kB](http://static.zybuluo.com/candycat/0y9xt8awtvueymd63g829vmu/gaussian_blur.png)
图12.7 左图：原效果。右图：高斯模糊后的效果

![gaussian_kernel.png-21.2kB](http://static.zybuluo.com/candycat/qdi1a1gaicihr3tju2acbcdc/gaussian_kernel.png)
图12.8 一个5×5大小的高斯核。左图显示了标准方差为1的高斯核的权重分布。我们可以把这个二维高斯核拆分成两个一维的高斯核（右图）

![800px-Elephants_Dream_-_Emo_and_Proog.jpg-41.9kB](http://static.zybuluo.com/candycat/0k9u1k5rrg9cq4gj4mwj1l0x/800px-Elephants_Dream_-_Emo_and_Proog.jpg)
图12.9 动画短片《大象之梦》中的Bloom效果。光线透过门扩散到了周围较暗的区域中

![bloom.png-772.3kB](http://static.zybuluo.com/candycat/gt2h3xoo89hmvm8o85pso5uh/bloom.png)
图12.10 左图：原效果。右图：Bloom处理后的效果

![motion_blur.png-770.9kB](http://static.zybuluo.com/candycat/ryde8k1k1bm5j7dxgdo5w0ks/motion_blur.png)
图12.11 左图：原效果。右图：应用运动模糊后的效果





### 第13章 使用深度和法线纹理





![projection_matrix.png-150.4kB](http://static.zybuluo.com/candycat/u6fma5c4boo56dgjbgczlb2i/projection_matrix.png)
图13.1 在透视投影中，投影矩阵首先对顶点进行了缩放。在经过齐次除法后，透视投影的裁剪空间会变换到一个立方体。图中标注了4个关键点经过投影矩阵变换后的结果

![orthographic_matrix.png-129.6kB](http://static.zybuluo.com/candycat/8idbd0mykpsqnj16t84uwsml/orthographic_matrix.png)
图13.2 在正交投影中，投影矩阵对顶点进行了缩放。在经过齐次除法后，正交投影的裁剪空间会变换到一个立方体。图中标注了4个关键点经过投影矩阵变换后的结果

![check_texture.png-161.3kB](http://static.zybuluo.com/candycat/xnqw3nkojdxml562evws8aug/check_texture.png)
图13.3 使用Frame Debugger查看深度纹理（左）和深度+法线纹理（右）。如果当前摄像机需要生成深度和法线纹理，帧调试器的面板中就会出现相应的渲染事件。只要单击对应的事件就可以查看得到的深度和法线纹理

![check_texture_code.png-84kB](http://static.zybuluo.com/candycat/kp57syi72i7jloyghgbeqy82/check_texture_code.png)
图13.4 左图：线性空间下的深度纹理。右图：解码后并且被映射到[0, 1]范围内的视角空间下的法线纹理

![fog.png-627.5kB](http://static.zybuluo.com/candycat/6yzf4h789v3117qpa4t2k931/fog.png)
图13.5 左图：原效果。右图：添加全局雾效后的效果

![frustum.png-33.5kB](http://static.zybuluo.com/candycat/cisfq83ut1mx2ou313e1nqg2/frustum.png)
图13.6 计算interpolatedRay

![world_dist.png-18.6kB](http://static.zybuluo.com/candycat/6h2nnw3gwzcio21jbji2o2dw/world_dist.png)
图13.7 采样得到的深度值并非是点到摄像机的欧式距离

![over_edge.png-819kB](http://static.zybuluo.com/candycat/20oe6ovk2wn4ko2el5ldwfs9/over_edge.png)
图13.8 左图：原效果。右图：直接对颜色图像进行边缘检测的结果

![edge_detect.png-452.9kB](http://static.zybuluo.com/candycat/snzxjfahsz29po5mcrfrczmu/edge_detect.png)
图13.9 在深度和法线纹理上进行更健壮的边缘检测。左图：在原图上描边的效果。右图：只显示描边的效果

![Roberts.png-15.7kB](http://static.zybuluo.com/candycat/ziah5yj1twj4nva7ldvw8dnk/Roberts.png)
图13.10 Roberts算子





### 第14章 非真实感渲染





![okami_announce_screens6.jpg-169.9kB](http://static.zybuluo.com/candycat/aa2hjqkoibcqmq5g5azdkrfb/okami_announce_screens6.jpg)
图14.1 游戏《大神》（英文名：Okami）的游戏截图

![toon_shading.png-74.1kB](http://static.zybuluo.com/candycat/0x7o2vyl6fn74gwtunvdgufp/toon_shading.png)
图14.2 卡通风格的渲染效果

![antialiasing.png-138.4kB](http://static.zybuluo.com/candycat/z8c9f6kzclslbl0wdw7gxach/antialiasing.png)
图14.3 左图：未对高光区域进行抗锯齿处理。右图：使用fwidth函数对高光区域进行抗锯齿处理

![TAM.png-127.6kB](http://static.zybuluo.com/candycat/9h63lflg1a7f759pw5cwfqvz/TAM.png)
图14.4 一个TAM的例子（来源：Praun E, et al. Real-time hatching[4](http://static.zybuluo.com/candycat/qwr4r6aglmod38w2k1e0dq7h/CopyDataToGPU.png)）

![hatching.png-268.1kB](http://static.zybuluo.com/candycat/60jzr7ly5yqqcg09rfrc3icb/hatching.png)
图14.5 素描风格的渲染效果





### 第15章 使用噪声





![burn.png-429.1kB](http://static.zybuluo.com/candycat/43pgznadojl5el7s23zpki7x/burn.png)
图15.1 箱子的消融效果

![burn_noise.png-84.8kB](http://static.zybuluo.com/candycat/l8caf290oitxfnenqu38ed95/burn_noise.png)
图15.2 消融效果使用的噪声纹理

![water.png-722.5kB](http://static.zybuluo.com/candycat/rgxn8cpsc4isivqouvbxtev7/water.png)
图15.3 包含菲涅耳反射的水面波动效果。在左图中，视角方向和水面法线的夹角越大，反射效果越强。在右图中，视角方向和水面法线的夹角越大，折射效果越强

![cubemap.png-128.3kB](http://static.zybuluo.com/candycat/lh1zewua7dl2p8olhmctowoz/cubemap.png)
图15.4 本例使用的立方体纹理

![water_noise.png-202kB](http://static.zybuluo.com/candycat/unuc9j0kp9fffr7jcnbowvzi/water_noise.png)
图15.5 水波效果使用的噪声纹理。左图：噪声纹理的灰度图。右图：由左图生成的法线纹理

![fog.png-493.9kB](http://static.zybuluo.com/candycat/dmrvnch1muikmc6f50sdwdho/fog.png)
图15.6 左图：均匀雾效。右图：使用噪声纹理后的非均匀雾效

![fog_noise.jpg-13kB](http://static.zybuluo.com/candycat/kfctu0s78fl2pepr9h1hgjpo/fog_noise.jpg)
图15.7 本节使用的噪声纹理





### 第16章 Unity中的渲染优化技术





![render_static_window.png-156.1kB](http://static.zybuluo.com/candycat/mw2e3pfqk097fps9wbcwv8ff/render_static_window.png)
图16.1 Unity 5的渲染统计窗口

![profiler.png-122.5kB](http://static.zybuluo.com/candycat/f1fpglqqgcg7q17tum55e8bh/profiler.png)
图16.2 使用Unity的性能分析器中的渲染区域来查看更多关于渲染的统计信息

![frame_debugger.png-84.3kB](http://static.zybuluo.com/candycat/3qa6mzh0mc1q7jiqhaf3j7mv/frame_debugger.png)
图16.3 使用帧调试器来查看单独的draw call的绘制结果

![dynamic_batching0.png-138.9kB](http://static.zybuluo.com/candycat/ytyrujgdcz4dxpvm8nw3tibd/dynamic_batching0.png)
图16.4 动态批处理

![dynamic_batching1.png-138.9kB](http://static.zybuluo.com/candycat/0l9c6cjb4czi02hxr8e2ij0o/dynamic_batching1.png)
图16.5 多光源对动态批处理的影响结果

![static_batching0.png-112.9kB](http://static.zybuluo.com/candycat/h7pzd9j05aelvv6cafs7juzv/static_batching0.png)
图16.6 静态批处理前的渲染统计数据

![mark_static.png-22.3kB](http://static.zybuluo.com/candycat/jkgbb245hcnoxzq4k3go3yba/mark_static.png)
图16.7 把物体标志为Static

![static_batching1.png-112.3kB](http://static.zybuluo.com/candycat/p7h3m5syxv9g7i928zohzhas/static_batching1.png)
图16.8 静态批处理

![combined_mesh.png-152.1kB](http://static.zybuluo.com/candycat/kfz63didqcnctti7ft8lvtpw/combined_mesh.png)
图16.9 静态批处理中Unity会合并所有被标识为“Static”的物体

![vbo.png-92kB](http://static.zybuluo.com/candycat/u9o9tk9oispyksk3ag41an3x/vbo.png)
图16.10 静态批处理会占用更多的内存。左图：静态批处理前的渲染统计数据。右图：静态批处理后的渲染统计数据

![static_batching2.png-113.6kB](http://static.zybuluo.com/candycat/zul250cb0n5x5w5821tu4xwd/static_batching2.png)
图16.11 处理其他逐像素光的Pass不会被静态批处理

![advance_texture.png-96.6kB](http://static.zybuluo.com/candycat/58dcw7v9r39i2p2izrtxq5bs/advance_texture.png)
图16.12 Unity的高级纹理设置面板





### 第17章 Surface Shader探秘





![bumped_diffuse.png-164.7kB](http://static.zybuluo.com/candycat/slo759tsffn90428bqqkt054/bumped_diffuse.png)
图17.1 表面着色器的例子。左图：在一个平行光下的效果。右图：添加了一个点光源（蓝色）和一个聚光灯（紫色）后的效果

![generated_code.png-28.9kB](http://static.zybuluo.com/candycat/rt3i7s74tdilo8185rexkowi/generated_code.png)
图17.2 查看表面着色器生成的代码

![pipeline.png-171.9kB](http://static.zybuluo.com/candycat/rokaz0qqzk11hyj7ntkss3ze/pipeline.png)
图17.3 表面着色器的渲染计算流水线。黄色：可以自定义的函数。灰色：Unity自动生成的计算步骤

![normal_extrusion.png-127.3kB](http://static.zybuluo.com/candycat/bhggsxnr7rlhkzs8u68mqarn/normal_extrusion.png)
图17.4 沿顶点法线对模型进行膨胀。左图：膨胀前。右图：膨胀后





### 第18章 基于物理的渲染





![reflect_refract.png-26.9kB](http://static.zybuluo.com/candycat/nw3v0p25h9165552cshmr1t1/reflect_refract.png)
图18.1 在理想的边界处，折射率的突变会把光线分成两个方向

![rought_smooth.png-64.6kB](http://static.zybuluo.com/candycat/zmrvmeo27ach7kjpxm1grnwb/rought_smooth.png)
图18.2 左图：光滑表面的微平面的法线变化较小，反射光线的方向变化也更小。 右图：粗糙表面的微平面的法线变化较大，反射光线的方向变化也更大

![subsurface_scattered_light.png-36.3kB](http://static.zybuluo.com/candycat/ezo6d9xa3vv6l97hdy48jltc/subsurface_scattered_light.png)
图18.3 微表面对光的折射。这些被折射的光中一部分被吸收，一部分又被散射到外部

![surface.png-42.5kB](http://static.zybuluo.com/candycat/th1ophcgurbsh1jbobzz2d6k/surface.png)
图18.4 次表面散射。左图：次表面散射的光线会从不同于入射点的位置射出。如果这些距离值小于需要被着色的像素大小，那么渲染就可以完全在局部完成（右图）。否则，就需要使用次表面散射渲染技术

![brdf.png-47.1kB](http://static.zybuluo.com/candycat/08orrgge69y3d3zgp4gfpcn9/brdf.png)
图18.5 BRDF描述的两种现象。高光反射部分用于描述反射，漫反射部分用于描述次表面散射

![m_h.png-90.5kB](http://static.zybuluo.com/candycat/d03qynt6prxeq7cep9b1jl91/m_h.png)
图18.6 （a）那些m=h的微面元会恰好把入射光从I反射到v上，只有这部分微面元才可以添加到BRDF的计算中。（b）一部分满足（a）的微面元会在I方向上被其他微面元遮挡住，它们不会接受到光照，因此会形成阴影。（c）还有一部分满足（a）的微面元会在反射方向v上被其他微面元挡住，因此，这部分反射光也不会被看到

![standard_shader.png-276.6kB](http://static.zybuluo.com/candycat/8yd8tgsx8x1tvdcwuxxowgt3/standard_shader.png)
图18.7 Standard Shader中前向渲染路径使用的Pass（简化版本的PBS使用了VertexOutputBaseSimple等结构体来代替相应的结构体）

![calibration_charts.png-387.8kB](http://static.zybuluo.com/candycat/kpx9eqzt6xjtw7lp9uac9qc8/calibration_charts.png)
图18.8 Unity提供的校准表格。左图：金属工作流 使用的校准表格。右图：高光反射工作流使用的校准表格

![metallic_workflow.png-181.6kB](http://static.zybuluo.com/candycat/0y8tojxhwa92hjy4oo20ii9p/metallic_workflow.png)
图18.9 使用金属工作流来实现不同类型的材质。左边的球体：金属材质。右边的球体：塑料材质

![pbs_scene.png-625.7kB](http://static.zybuluo.com/candycat/rre47eai63qgeh811clxbev2/pbs_scene.png)
图18.10 在Unity 5中使用基于物理的渲染技术，场景在不同光照下的渲染结果

![lighting_inspector.png-48.9kB](http://static.zybuluo.com/candycat/829ewyjmvzjm082xpyysvqfz/lighting_inspector.png)
图18.11 光照面板下的Scene标签页

![reflect_source.png-349.6kB](http://static.zybuluo.com/candycat/nlh6q7gqgwlbitske1z8938i/reflect_source.png)
图18.12 左图：当关闭场景中的所有光源并把环境光照强度设为0后，使用了Standard Shader的物体仍然具有光照效果。右图：在左图的基础上，把反射源设置为空，使得物体不接受任何默认的反射信息

![direction_light.png-29.3kB](http://static.zybuluo.com/candycat/x7cxbmmb2xdzke3m0asowtu9/direction_light.png)
图18.13 使用的平行光

![bounce_intensity.png-645.9kB](http://static.zybuluo.com/candycat/61ycjyc3k04bjh8sai6womkn/bounce_intensity.png)
图18.14 左图：将Bounce Intensity设置为0，物体不再受到间接光照的影响，木屋内阴影部分的可见细节很少。右图：将Bounce Intensity设为8，阴影部分的细节更加清楚

![reflection_probe.png-615.8kB](http://static.zybuluo.com/candycat/twic91rz1143c14rc0t1n1ie/reflection_probe.png)
图18.15 左图：未使用反射探针。右图：在场景中放置了两个反射探针，注意墙上的盾牌与左图的差别

![interreflection.png-338.2kB](http://static.zybuluo.com/candycat/d7amfp6yscz10g5yk0kybwd1/interreflection.png)
图18.16 使用反射探针实现相互反射的效果

![linear_space.png-611.4kB](http://static.zybuluo.com/candycat/umachb7kklgerrvsphv7yyoj/linear_space.png)
图18.17 左图：在线性空间下的渲染结果。右图：在伽马空间下的渲染结果

![gamma_chart.png-29.3kB](http://static.zybuluo.com/candycat/uizo2ug3l5ovy68zbn9afde0/gamma_chart.png)
图18.18 人眼更容易感知暗部区域的变换，而对较亮区域的变化比较不敏感

![encoding_display_gamma.png-37.5kB](http://static.zybuluo.com/candycat/2y5h6wx9hupw5nv2ugtseyqn/encoding_display_gamma.png)
图18.19 编码伽马和显示伽马

![gamma_light.png-32.1kB](http://static.zybuluo.com/candycat/xuxe7bp91pykknxybt6yu2wu/gamma_light.png)
图18.20 左图：伽马空间下的渲染结果。右图：线性空间下的渲染结果

![gamma_blur.png-85.2kB](http://static.zybuluo.com/candycat/a4e1xfpbxduwotib6o4dty5s/gamma_blur.png)
图18.21 左图：伽马空间下的混合结果。右图：线性空间下的混合结果





### 第19章 Unity 5更新了什么





![show_fixed_function.png-29.5kB](http://static.zybuluo.com/candycat/wosup72bju19rx6rkucnk7y6/show_fixed_function.png)
图19.1 在shader的导入面板中，单击图中按钮可查看Unity为该固定管线着色器生成的顶点/片元着色器代码B](http://static.zybuluo.com/candycat/xuxe7bp91pykknxybt6yu2wu/gamma_light.png)
图18.20 左图：伽马空间下的渲染结果。右图：线性空间下的渲染结果

![gamma_blur.png-85.2kB](http://static.zybuluo.com/candycat/a4e1xfpbxduwotib6o4dty5s/gamma_blur.png)
图18.21 左图：伽马空间下的混合结果。右图：线性空间下的混合结果





### 第19章 Unity 5更新了什么





![show_fixed_function.png-29.5kB](http://static.zybuluo.com/candycat/wosup72bju19rx6rkucnk7y6/show_fixed_function.png)
图19.1 在shader的导入面板中，单击图中按钮可查看Unity为该固定管线着色器生成的顶点/片元着色器代码
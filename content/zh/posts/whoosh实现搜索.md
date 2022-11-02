---
title: "whoosh实现搜索功能"
summary: whoosh实现搜索功能
date: 2022-11-2
tags: ["whoosh"]
author: "YSL"
draft: false
weight: 2
---

### 创造字典

```python
# jsonDictList 数据
# schema 设置作为搜索依据的内容
def createSearch(jsonDictList):
    schema = Schema(
                        title=TEXT(stored=True, analyzer=ChineseAnalyzer()),
                        url = ID(stored=True),
                    )
            # # 存储schema信息至indexdir目录
            
    if not os.path.exists(indexdir):
        os.mkdir(indexdir)
    ix = create_in(indexdir, schema)
    # # # 按照schema定义信息，增加需要建立索引的文档
    writer = ix.writer()
    for jsonDict in jsonDictList:
        writer.add_document(title=jsonDict["title"],url = jsonDict["url"])
    writer.commit()
```

### 搜索内容

```python
def searchByTitle(title):
    ix = index.open_dir(indexdir)
    # 创建一个检索器
    searcher = ix.searcher()
    # 检索
    results = searcher.find("title", title,limit=None)
    resultsList = []
    print('一共发现%d个稿件。' % len(results))
    for res in results:
        resultsList.append(res.fields())
    return resultsList
```

### 更新内容

```python
#jsonDictList 更新的数据
def updateSearch(jsonDictList):
    ix = index.open_dir(indexdir)
    writer = ix.writer()
    for jsonDict in jsonDictList:
        writer.add_document(title=jsonDict["title"],url = jsonDict["url"])
    writer.commit()
```


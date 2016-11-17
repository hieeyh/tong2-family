1.概括
	index2QQ_id位每个用户的编号到QQ号的映射
	atCount为用户互相@的计数
	dayVector为每个用户平均每天的发言密度，统计以6分钟为一个单元，一天分为240个单元，储存在一个240个元素的向量里面
	similarityMatrix为用户间的亲密度（0-100）
	
2.详细信息
	2.1 index2QQ_id是一个map（字典）结构，key为用户编号，value为用户的QQ号
	2.2 dayVector是一个二维数组，第i行的第j个元素储存的是编号为i的用户平均每天在第j个6分钟的发言计数
	2.3 atCount是一个二维数组，第i行的第j个元素储存的是编号为i的用户@编号为j的用户的次数
	2.4 similarityMatrix是一个二维数组，第i行的第j个元素储存的是编号为i的用户和编号为j的用户的亲密度
	
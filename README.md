# need-for-auto-speed

## 阶段一：无目的的全速roaming race

* 车道识别，反馈进行当前水平方向纠正
* 简单控制，纠正方向

## 阶段二：带障碍识别的无目的变速roaming race

* 物体识别，反馈进行当前垂直方向加减速和水平方向纠正
* 简单控制，增加撞车后倒车重启逻辑

## 阶段三：可增加目标坐标的race

* 简单控制，往目标坐标贪婪逼近
* visual slam，建立基于visual slam的地图

## 阶段四：增加对目标坐标寻路的race

* visual slam建立完成后增加导航
* 加入其他sensing的基于kalman filter的控制

## 阶段五：竞争竞速

* 其他可能的基于竞争的驾驶策略

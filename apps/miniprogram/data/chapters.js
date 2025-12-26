// chapters.js - 专题数据

const chapterList = [
  {
    id: 1,
    name: '专题一：有理数',
    desc: '数轴、绝对值、相反数',
    icon: '📊',
    color: '#3B82F6',
    count: 7,
    techniques: [
      { id: 't1', name: '考法1', title: '数轴上的整点与动点问题', trainCount: 3 },
      { id: 't2', name: '考法2', title: '数轴上的规律探究', trainCount: 2 },
      { id: 't3', name: '考法3', title: '绝对值与大小比较', trainCount: 3 },
      { id: 't4', name: '考法4', title: '绝对值的化简', trainCount: 2 },
      { id: 't5', name: '考法5', title: '绝对值的几何意义', trainCount: 2 },
      { id: 't6', name: '考法6', title: '新定义问题', trainCount: 2 },
      { id: 't7', name: '考法7', title: '实际应用问题', trainCount: 2 }
    ]
  },
  {
    id: 2,
    name: '专题二：有理数的运算',
    desc: '运算技巧与数轴问题',
    icon: '🔢',
    color: '#10B981',
    count: 8,
    techniques: [
      // 考点1：有理数的运算技巧
      { id: 't8', name: '考点1-考法1', title: '拼凑法', trainCount: 3 },
      { id: 't9', name: '考点1-考法2', title: '裂项相消法', trainCount: 3 },
      { id: 't10', name: '考点1-考法3', title: '倒数法和运算律', trainCount: 2 },
      { id: 't11', name: '考点1-考法4', title: '混合运算', trainCount: 3 },
      // 考点2：数轴问题
      { id: 't12', name: '考点2-考法1', title: '数轴上的折叠问题', trainCount: 2 },
      { id: 't13', name: '考点2-考法2', title: '数轴动点问题', trainCount: 2 },
      // 考点3：绝对值综合
      { id: 't14', name: '考点3', title: '有理数的运算与绝对值的综合运用', trainCount: 2 },
      // 考点4：新定义问题
      { id: 't15', name: '考点4', title: '与有理数运算相关的新定义问题', trainCount: 2 }
    ]
  },
  {
    id: 3,
    name: '专题三：代数式',
    desc: '字母表示数、求值',
    icon: '📐',
    color: '#F59E0B',
    count: 5,
    techniques: [
      { id: 't16', name: '考点1', title: '用字母表示数', trainCount: 3 },
      { id: 't17', name: '考点2', title: '直接求值', trainCount: 3 },
      { id: 't18', name: '考点3', title: '整体思想', trainCount: 1 },
      { id: 't19', name: '考点4', title: '规律探究', trainCount: 3 },
      { id: 't20', name: '考点5', title: '代数式的新定义问题', trainCount: 1 }
    ]
  },
  {
    id: 4,
    name: '专题四：整式的加减',
    desc: '化简求值、规律探究',
    icon: '➕',
    color: '#EF4444',
    count: 4,
    techniques: [
      { id: 't21', name: '考法1', title: '整体思想', trainCount: 2 },
      { id: 't22', name: '考法2', title: '数轴化简', trainCount: 2 },
      { id: 't23', name: '考法3', title: '分类讨论', trainCount: 2 },
      { id: 't24', name: '考法4', title: '围棋规律探究', trainCount: 2 }
    ]
  },
  {
    id: 5,
    name: '专题五：一元一次方程',
    desc: '方程应用与技巧',
    icon: '⚖️',
    color: '#8B5CF6',
    count: 14,
    techniques: [
      // 考点1：解方程技巧
      { id: 't25', name: '考点1-考法1', title: '用整体思想解一元一次方程', trainCount: 2 },
      { id: 't26', name: '考点1-考法2', title: '裂项相消法解方程', trainCount: 2 },
      { id: 't27', name: '考点1-考法3', title: '绝对值方程的分类讨论', trainCount: 2 },
      // 考点2：方程应用基础
      { id: 't28', name: '考点2-考法1', title: '销售利润问题', trainCount: 2 },
      { id: 't29', name: '考点2-考法2', title: '行程问题', trainCount: 2 },
      { id: 't30', name: '考点2-考法3', title: '工程问题', trainCount: 2 },
      { id: 't31', name: '考点2-考法4', title: '方案设计问题', trainCount: 2 },
      // 考点3：方程解的关系
      { id: 't38', name: '考点3-考法1', title: '两个一元一次方程解的关系', trainCount: 2 },
      { id: 't39', name: '考点3-考法2', title: '方程变形', trainCount: 2 },
      { id: 't40', name: '考点3-考法3', title: '方程规律', trainCount: 2 },
      { id: 't41', name: '考点3-考法4', title: '方程应用进阶', trainCount: 2 },
      // 考点4：复杂应用
      { id: 't42', name: '考点4-考法1', title: '调配配套问题', trainCount: 2 },
      { id: 't43', name: '考点4-考法2', title: '工程问题进阶', trainCount: 2 },
      { id: 't44', name: '考点4-考法3', title: '行程问题进阶', trainCount: 2 }
    ]
  },
  {
    id: 6,
    name: '专题六：几何图形初步',
    desc: '线段、角度计算',
    icon: '📏',
    color: '#EC4899',
    count: 6,
    techniques: [
      // 考点1：线段计算
      { id: 't32', name: '考点1-考法1', title: '整体思想在线段计算中的应用', trainCount: 2 },
      { id: 't33', name: '考点1-考法2', title: '方程思想', trainCount: 2 },
      { id: 't34', name: '考点1-考法3', title: '分类讨论思想', trainCount: 2 },
      { id: 't35', name: '考点1-考法4', title: '数形结合思想', trainCount: 2 },
      // 考点2：角度计算
      { id: 't36', name: '考点2-考法1', title: '数学思想在角度计算中的应用', trainCount: 2 },
      { id: 't37', name: '考点2-考法2', title: '旋转角度问题', trainCount: 2 }
    ]
  }
]

module.exports = {
  chapterList
}

let groups = {}; // Remplacer par une base de données en production

export default (req, res) => {
  const { groupId, name, email } = req.body;

  if (!groups[groupId]) {
    groups[groupId] = [];
  }

  groups[groupId].push({ name, email });
  res.status(200).json({ message: 'Participant ajouté' });
};
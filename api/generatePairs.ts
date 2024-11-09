import shuffle from 'lodash.shuffle';

export default (req, res) => {
  const { groupId } = req.body;
  const participants = groups[groupId];

  if (!participants || participants.length < 2) {
    res.status(400).json({ message: 'Pas assez de participants' });
    return;
  }

  const shuffled = shuffle(participants);
  const pairs = shuffled.map((participant, i) => ({
    giver: participant,
    receiver: shuffled[(i + 1) % shuffled.length]
  }));

  res.status(200).json({ pairs });
};